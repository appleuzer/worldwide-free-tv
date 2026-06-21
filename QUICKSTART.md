# 🌍 Worldwide Free TV — Quick Start

Watch live TV from all over the world, free, in your browser. This guide gets you up and running in a couple of minutes.

---

## ✅ What you need

- **Python 3** — already installed on most Macs and Linux machines. Check with:
  ```bash
  python3 --version
  ```
- A modern browser (Chrome, Edge, Firefox, Safari, or Opera).

That's it. No accounts, no installs, no dependencies.

---

## 🚀 Start watching

### The easy way (macOS / Linux)

```bash
git clone https://github.com/appleuzer/worldwide-free-tv.git
cd worldwide-free-tv
./start.sh
```

Your browser pops open at **http://localhost:8000** and you're watching TV. 🎉

### The manual way (any OS, including Windows)

```bash
python3 server.py
```

Then open **http://localhost:8000/index.html** in your browser.

To stop the server, press **Ctrl+C** in the terminal.

> ⚠️ **Don't double-click `index.html`.** It must be served through `server.py`, otherwise the browser shows "Failed to fetch" and streams won't play. See [Why a server?](#-why-do-i-need-the-server) below.

---

## 🎮 How to use it

### Browse the world

- **Filter by country** — click a country in the sidebar (United States, Germany, Ukraine, Japan…) to see only its channels.
- **Filter by genre** — pick a category like News, Sports, Movies, Music, or Kids.
- **Search** — type anything in the search box; results filter as you type.
- **Sort** — order the list by Name, Country, or Genre.

### Watch like it's a real TV

| Action | How |
|---|---|
| ▶️ Play / pause | `Space` |
| ⬆️ Previous channel | `↑` arrow, or **◀ Previous** button |
| ⬇️ Next channel | `↓` arrow, or **Next ▶** button |
| 🖥️ Fullscreen | `F`, or the **Fullscreen** button |
| 🔄 Retry a stuck stream | `R`, or the **Retry** button |

### It remembers you

Your last channel, country filter, and genre are saved automatically. Next time you open it, you're right back where you left off — playing the last channel that actually worked.

### It skips dead channels

Some public streams go offline or are geo-blocked. If a channel fails to load, the app automatically jumps to the next one, so you're never stuck staring at a spinner.

---

## 🛰️ Why do I need the server?

A plain HTML file can't do this on its own because of two browser rules. The included `server.py` handles both for you:

1. **Browsers block local file access** — Chrome won't let a `file://` page load the playlist. Serving it from `http://localhost` fixes that.
2. **TV streams block cross-site requests** — most IPTV servers don't send the `CORS` headers browsers require. `server.py` works as a small local proxy: it fetches each stream itself and re-serves it with the correct headers, and rewrites HLS playlists so every video segment flows back through it.

It's one small, dependency-free Python file. Nothing to install.

---

## 🔄 Want more channels?

The bundled `playlist.m3u` is a snapshot from the open [iptv-org](https://github.com/iptv-org/iptv) project. To refresh or expand it:

```bash
# Solid starter set (~950 channels)
curl -s "https://iptv-org.github.io/iptv/index.m3u" | head -2000 > playlist.m3u

# More channels (~1,200)
curl -s "https://iptv-org.github.io/iptv/index.m3u" | head -5000 > playlist.m3u

# Everything (~10,000+ channels worldwide)
curl -s "https://iptv-org.github.io/iptv/index.m3u" > playlist.m3u
```

Then click **🗑️ Clear Cache** in the app (or just wait — it auto-refreshes every 24 hours).

---

## 🧯 Troubleshooting

| Symptom | What to do |
|---|---|
| "Failed to fetch" or a blank channel list | You opened `index.html` directly. Use `./start.sh` or `python3 server.py`, then visit **http://localhost:8000**. |
| A channel won't load | It may be offline or geo-blocked — the app auto-skips. Channels tagged `[Geo-blocked]` or `[Not 24/7]` are unreliable. |
| Video plays but no sound | Some minimal browser builds lack certain audio codecs; standard Chrome/Edge/Safari play audio fine. |
| Slow first load | The playlist is fetched once, then cached. After that it loads instantly. |
| Port 8000 already in use | Stop whatever is using it, or change `PORT` near the top of `server.py`. |

---

## 🎯 TL;DR

```bash
git clone https://github.com/appleuzer/worldwide-free-tv.git
cd worldwide-free-tv
./start.sh
```

Pick a country, pick a channel, and enjoy free TV from around the world. 🌍📺
