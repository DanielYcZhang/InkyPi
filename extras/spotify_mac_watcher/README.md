# Spotify Mac Watcher

1. Copy `.env.example` to `.env`.
2. Set `PI_BASE_URL` and `SPOTIFY_PUSH_TOKEN`.
3. Run `python3 spotify_mac_watcher.py`.
4. Install or repair the login service with `bash install_launch_agent.sh`.

The installer creates a LaunchAgent for the logged-in macOS session, starts it immediately, and configures it to restart automatically. Its persistent log is stored at `~/Library/Logs/InkyPi/spotify-mac-watcher.log` so reboot diagnostics are not lost with `/tmp`.

The watcher sends a lightweight heartbeat every 60 seconds by default. This lets the Pi detect when the Mac sleeps or disconnects without refreshing the display for every heartbeat. Override it with `HEARTBEAT_SECONDS` if needed.

Failed track updates retry every 5 seconds by default without bypassing the track-change debounce. Override this with `RETRY_INTERVAL_SECONDS` if needed.
