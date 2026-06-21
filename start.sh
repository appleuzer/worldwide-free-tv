#!/bin/bash
# Easy launcher for the IPTV player.
# Starts the local server + CORS proxy and opens the player in your browser.

cd "$(dirname "$0")"

echo "Starting IPTV server..."
# Open the browser after a short delay (server needs a moment to boot)
( sleep 1.5 && open "http://localhost:8000/index.html" ) &

python3 server.py
