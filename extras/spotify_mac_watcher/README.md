# Spotify Mac Watcher

1. Copy `.env.example` to `.env`.
2. Set `PI_BASE_URL` and `SPOTIFY_PUSH_TOKEN`.
3. Run `python3 spotify_mac_watcher.py`.
4. Install or repair the login service with `bash install_launch_agent.sh`.

The installer creates a LaunchAgent for the logged-in macOS session, starts it immediately, and configures it to restart automatically. Its persistent log is stored at `~/Library/Logs/InkyPi/spotify-mac-watcher.log` so reboot diagnostics are not lost with `/tmp`.

After installing, open **System Settings > General > Login Items & Extensions** and make sure `inkypi-spotify-watcher` (or **Unknown Developer**) is enabled under **Allow in Background**. macOS can run a manually installed agent for the current session while still blocking it after the next reboot, so this permission is required for reliable login startup.

Run `bash check_status.sh` at any time to check the watcher process, macOS background permission, last successful Pi update, and Pi connectivity. If it reports that the watcher is not running, repair it with `bash install_launch_agent.sh`.

The watcher sends a lightweight heartbeat every 60 seconds by default. This lets the Pi detect when the Mac sleeps or disconnects without refreshing the display for every heartbeat. Override it with `HEARTBEAT_SECONDS` if needed.

Failed track updates retry every 5 seconds by default without bypassing the track-change debounce. Override this with `RETRY_INTERVAL_SECONDS` if needed.

AppleScript probes time out after 8 seconds by default so a stuck Spotify automation request cannot freeze the watcher forever. Override this with `APPLESCRIPT_TIMEOUT_SECONDS` if necessary.
