# IPTV Live TV Player

A fast, lightweight HTML-based TV watching interface with support for M3U playlists and channel filtering.

## Features

✅ **Live Video Playback** - YouTube-like video controls (play, pause, stop, fullscreen)
✅ **Fast Loading** - Single HTML file, loads instantly
✅ **Channel Search** - Real-time search across channel names, countries, and types
✅ **Smart Filtering** - Filter by country (50+ countries) or channel type (25+ categories)
✅ **Sorting Options** - Sort by name, country, or type
✅ **Channel Logos** - Visual channel identification with thumbnail logos
✅ **Responsive Layout** - Desktop-optimized UI with retro cyan terminal aesthetics
✅ **M3U Support** - Automatically parses and loads IPTV playlists
✅ **Browser Compatible** - Works in all modern browsers (Chrome, Firefox, Safari, Edge)

## Current Status: ✅ WORKING!

**Tested Features:**
- ✅ 953 channels loaded from local M3U playlist
- ✅ Country filtering (50+ countries: US, UK, CA, AU, DE, etc.)
- ✅ Type filtering (25+ categories: Movies, Sports, News, Documentary, etc.)
- ✅ Real-time search working perfectly
- ✅ Channel playback with full video controls
- ✅ Channel info display
- ✅ Fullscreen mode

## Getting Started

### Quick Start

1. **Both files required** - Make sure `index.html` AND `playlist.m3u` are in the same directory
2. **Open the file** - Simply open `index.html` in your web browser
3. **Wait for channels to load** - Channels load instantly from the local playlist
4. **Browse and play** - Click any channel to start watching

### Files Structure

```
/Users/appleuzer/iptv/
├── index.html          ← Open this in browser
├── playlist.m3u        ← Required M3U playlist (953 channels)
├── README.md           ← This file
└── QUICKSTART.md       ← User guide
```

### Usage

- **Search**: Type in the search box (e.g., "free movies", "news", "sports")
- **Filter by Country**: Click any country code (US, UK, CA, AU, DE, etc.)
- **Filter by Type**: Click a category (Movies, News, Sports, Documentary, etc.)
- **Sort**: Change sort order from dropdown (Name, Country, Type)
- **Play**: Click any channel to start watching
- **Controls**: Play, Pause, Stop, Fullscreen buttons

## How It Works

1. Loads M3U playlist from local `playlist.m3u` file
2. Parses channel metadata:
   - Extracts country codes from `tvg-id` (e.g., `.us`, `.uk`, `.ca`)
   - Splits `group-title` by semicolons for multiple categories
   - Loads channel logos from URLs
3. Filters and sorts locally in the browser
4. Streams video directly from source URLs
5. All processing happens client-side (no server required)

## Data Sources

- **Playlist**: Local M3U file (`playlist.m3u`) - 953 channels included
  - Original source: https://iptv-org.github.io/iptv/index.m3u
  - First 2000 lines (~953 channels) for fast loading

## Updating the Playlist

To get more channels or update the playlist:

```bash
# Download first 2000 lines (~500 channels)
curl -s "https://iptv-org.github.io/iptv/index.m3u" | head -2000 > playlist.m3u

# Download first 5000 lines (~1200 channels)  
curl -s "https://iptv-org.github.io/iptv/index.m3u" | head -5000 > playlist.m3u

# Download full playlist (~25000 lines, may take 10-30 seconds to load)
curl -s "https://iptv-org.github.io/iptv/index.m3u" > playlist.m3u
```

## Browser Requirements

- Modern browser with HLS/HTTP streaming support
- JavaScript enabled
- Good internet connection for streaming (recommended: 5+ Mbps)

## Troubleshooting

**Channels not loading?**
- Make sure `playlist.m3u` exists in the same directory as `index.html`
- Check browser console (F12) for error messages
- Try refreshing the page

**Video not playing?**
- Some streams may be geo-blocked or offline
- Try a different channel to test
- Check your internet connection

**Search shows nothing?**
- Make sure you typed the search term correctly
- Try broader terms (e.g., "news" instead of "bbc news")
- Clear the search and try filtering by type instead

## Performance Tips

- Current playlist (953 channels) loads instantly
- Filter by country to narrow down results
- Use search for quick channel finding
- Downloads only what's needed (no full playlist fetch unless you update)

## License

This player is a simple frontend for the IPTV M3U playlist project.
Respects all terms of the original IPTV project.

---

**Last Updated**: 2026-06-20  
**Version**: 1.0.0 (Working)
