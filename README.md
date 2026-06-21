# 🌍 Worldwide Free TV

**Watch live television from around the planet — for free, right in your browser.**

Worldwide Free TV is a fast, lightweight web app that turns the open [iptv-org](https://github.com/iptv-org/iptv) channel list into a slick, TV-like watching experience. Hundreds of channels from dozens of countries — news, sports, movies, music, kids, and more — all just a click away. No account. No subscription. No app store.

```
📺  Hundreds of channels   🌐  Dozens of countries   🆓  100% free   ⚡  Loads instantly
```

---

## ✨ Why you'll like it

- **🌎 Channels from everywhere** — browse by country and watch TV from the US, UK, Germany, Ukraine, Japan, Brazil, and many more.
- **🎚️ Channel surfing like a real TV** — arrow keys to flip channels, `F` for fullscreen, `Space` to pause. It feels like a remote.
- **🔎 Find anything fast** — instant search plus filters by country and genre (News, Sports, Movies, Music, Kids…).
- **⏭️ Dead streams? No problem** — if a channel is offline, it automatically skips to the next working one.
- **🧠 Remembers you** — your last channel, country, and genre are saved so you pick up right where you left off.
- **💾 Smart caching** — the channel list is cached locally and auto-refreshes every 24 hours, so it loads instantly.
- **🎬 Real video controls** — play, pause, fullscreen, and a clean cinematic layout.

---

## 🚀 Run it in 30 seconds

You need **Python 3** (already on most Macs and Linux machines). Then:

```bash
# 1. Clone the repo
git clone https://github.com/appleuzer/worldwide-free-tv.git
cd worldwide-free-tv

# 2. Start it (macOS/Linux)
./start.sh
```

That's it — your browser opens to **http://localhost:8000** and you're watching TV. 🎉

Prefer to do it manually, or on Windows?

```bash
python3 server.py
```

Then open **http://localhost:8000/index.html** in your browser. Press **Ctrl+C** in the terminal to stop.

> **Heads up:** you must run it through the included server (`server.py`) — don't just double-click `index.html`. The server quietly fixes two browser limitations for you (see [Why a server?](#-why-a-server) below).

---

## 🎮 Controls

| Action | How |
|---|---|
| Next / previous channel | `↑` / `↓` arrow keys, or the **Next / Previous** buttons |
| Play / pause | `Space` |
| Fullscreen | `F` |
| Retry current channel | `R` |
| Search | Type in the search box |
| Filter | Click a country or genre in the sidebar |

---

## 🛰️ Why a server?

Two things stop a TV app like this from "just working" as a plain HTML file — the included `server.py` solves both automatically:

1. **Browsers block local file access.** Chrome won't let a `file://` page load the playlist for security reasons. Serving over `http://localhost` fixes that.
2. **Most TV streams block cross-site requests.** Public IPTV servers don't send the `CORS` headers browsers require, so the browser refuses to play them. `server.py` acts as a tiny **local proxy**: it fetches each stream itself and re-serves it with the right headers, and rewrites HLS playlists so every video segment flows back through it.

It's a single, dependency-free Python file — no frameworks, nothing to install.

---

## 📦 What's inside

| File | Purpose |
|---|---|
| `index.html` | The entire app — UI, player, and logic in one file |
| `server.py` | Local web server **+ CORS stream proxy** |
| `start.sh` | One-command launcher (starts server, opens browser) |
| `playlist.m3u` | A snapshot of channels from the iptv-org project |
| `README.md` | This file |
| `QUICKSTART.md` | A friendly step-by-step guide |

---

## 🔄 Get more channels

The included `playlist.m3u` is a snapshot. To refresh it or grab more channels from the always-updated [iptv-org](https://github.com/iptv-org/iptv) list:

```bash
# A solid starter set (~950 channels, loads instantly)
curl -s "https://iptv-org.github.io/iptv/index.m3u" | head -2000 > playlist.m3u

# More channels (~1,200)
curl -s "https://iptv-org.github.io/iptv/index.m3u" | head -5000 > playlist.m3u

# The whole world (~10,000+ channels)
curl -s "https://iptv-org.github.io/iptv/index.m3u" > playlist.m3u
```

Then clear the cache with the **🗑️ Clear Cache** button (or just wait — it auto-refreshes every 24 hours).

---

## 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| "Failed to fetch" / nothing loads | You opened `index.html` directly. Run `./start.sh` or `python3 server.py` and use **http://localhost:8000** instead. |
| A channel won't play | Some streams are offline or geo-blocked — the app auto-skips. Channels tagged `[Geo-blocked]` or `[Not 24/7]` are hit-or-miss. |
| No sound but video plays | Some minimal browser builds lack certain audio codecs; normal Chrome/Edge/Safari play audio fine. |
| Slow to start | First load fetches the playlist; after that it's cached and instant. |

---

## 🌐 Works in

Chrome · Edge · Firefox · Safari · Opera — any modern desktop browser.

---

## 📜 Credits & license

Channel data comes from the wonderful open-source [**iptv-org/iptv**](https://github.com/iptv-org/iptv) community project. This app is just a friendly viewer on top of it — please respect the terms and notes of the upstream project and the individual broadcasters.

Made for fun. Watch the world. 🌍📺
