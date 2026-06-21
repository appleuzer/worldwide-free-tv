#!/usr/bin/env python3
"""
IPTV Local Server + CORS Proxy

Serves the index.html / playlist.m3u files AND proxies IPTV streams so the
browser can play them. Most IPTV streams don't send CORS headers, which makes
the browser refuse to load them. This proxy fetches the stream server-side
(no CORS restrictions) and re-serves it with the headers the browser needs.

For HLS (.m3u8) streams it rewrites all segment/sub-playlist URLs inside the
manifest so those requests also flow back through the proxy.

Usage:
    python3 server.py
Then open:  http://localhost:8000/index.html
"""

import http.server
import socketserver
import urllib.request
import urllib.parse
import urllib.error
import gzip
import io
import re
import ssl
import sys

PORT = 8000

# Many IPTV servers have broken, expired, or mismatched HTTPS certificates.
# A browser would refuse them, but for a local personal proxy we tolerate them
# so those channels still play. (This only affects streams fetched by the
# proxy, not your normal browsing.)
SSL_CONTEXT = ssl.create_default_context()
SSL_CONTEXT.check_hostname = False
SSL_CONTEXT.verify_mode = ssl.CERT_NONE

# A browser-like User-Agent. Many IPTV servers reject requests without one.
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
}


def is_m3u8(url, content_type):
    if content_type and ("mpegurl" in content_type.lower() or "vnd.apple" in content_type.lower()):
        return True
    # Strip query string before checking extension
    path = url.split("?", 1)[0].lower()
    return path.endswith(".m3u8")


def rewrite_manifest(body_text, base_url):
    """Rewrite all URLs in an HLS manifest to flow through /proxy."""
    out_lines = []
    for line in body_text.splitlines():
        stripped = line.strip()
        if not stripped:
            out_lines.append(line)
            continue

        # Handle URI="..." attributes (e.g. EXT-X-KEY, EXT-X-MEDIA)
        if stripped.startswith("#"):
            def repl_uri(m):
                orig = m.group(1)
                absolute = urllib.parse.urljoin(base_url, orig)
                return 'URI="/proxy?url=' + urllib.parse.quote(absolute, safe="") + '"'
            line = re.sub(r'URI="([^"]+)"', repl_uri, line)
            out_lines.append(line)
            continue

        # Otherwise this line is a media/playlist URL
        absolute = urllib.parse.urljoin(base_url, stripped)
        proxied = "/proxy?url=" + urllib.parse.quote(absolute, safe="")
        out_lines.append(proxied)

    return "\n".join(out_lines)


class ProxyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Quieter logging
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_OPTIONS(self):
        self.send_response(204)
        self._send_cors_headers()
        self.end_headers()

    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_GET(self):
        if self.path.startswith("/proxy?"):
            self.handle_proxy()
        else:
            # Serve static files normally
            super().do_GET()

    def handle_proxy(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        target = params.get("url", [None])[0]

        if not target:
            self.send_error(400, "Missing url parameter")
            return

        try:
            req = urllib.request.Request(target, headers=DEFAULT_HEADERS)
            with urllib.request.urlopen(req, timeout=15, context=SSL_CONTEXT) as resp:
                content_type = resp.headers.get("Content-Type", "")
                raw = resp.read()

                # Decompress if gzipped
                if resp.headers.get("Content-Encoding", "").lower() == "gzip":
                    try:
                        raw = gzip.decompress(raw)
                    except OSError:
                        pass

                if is_m3u8(target, content_type):
                    text = raw.decode("utf-8", errors="replace")
                    rewritten = rewrite_manifest(text, target)
                    body = rewritten.encode("utf-8")
                    self.send_response(200)
                    self._send_cors_headers()
                    self.send_header("Content-Type", "application/vnd.apple.mpegurl")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                else:
                    # Stream segments / other content through as-is
                    self.send_response(200)
                    self._send_cors_headers()
                    if content_type:
                        self.send_header("Content-Type", content_type)
                    self.send_header("Content-Length", str(len(raw)))
                    self.end_headers()
                    self.wfile.write(raw)

        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self._send_cors_headers()
            self.end_headers()
        except Exception as e:
            sys.stderr.write("Proxy error for %s: %s\n" % (target, e))
            try:
                self.send_response(502)
                self._send_cors_headers()
                self.end_headers()
            except Exception:
                pass


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    server = ThreadingHTTPServer(("", PORT), ProxyHTTPRequestHandler)
    print(f"\n  IPTV server running at: http://localhost:{PORT}/index.html")
    print(f"  Stream proxy active at: http://localhost:{PORT}/proxy?url=...")
    print("  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.shutdown()
