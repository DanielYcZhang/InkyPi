# Spotify Mac Watcher

1. Copy `.env.example` to `.env`.
2. Set `PI_BASE_URL` and `SPOTIFY_PUSH_TOKEN`.
3. Run `python3 spotify_mac_watcher.py`.
4. Optional: install the LaunchAgent plist after replacing the placeholder absolute paths.

The watcher sends a lightweight heartbeat every 60 seconds by default. This lets the Pi detect when the Mac sleeps or disconnects without refreshing the display for every heartbeat. Override it with `HEARTBEAT_SECONDS` if needed.
