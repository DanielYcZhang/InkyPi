# Spotify Now Playing

This integration has two parts:

1. InkyPi plugin: `Spotify Now Playing`
2. macOS watcher: `extras/spotify_mac_watcher/spotify_mac_watcher.py`

## Pi setup

1. Add `SPOTIFY_PUSH_TOKEN` to your `.env`.
2. Restart InkyPi so the new plugin and webhook are loaded.
3. Add the `Spotify Now Playing` plugin to a playlist.

The webhook endpoint is:

`POST /spotify_now_playing/update`

Send the shared secret in:

`X-InkyPi-Spotify-Token`

## Mac setup

1. Copy `extras/spotify_mac_watcher/.env.example` to `.env`.
2. Set `PI_BASE_URL` to your Pi's base URL.
3. Set `SPOTIFY_PUSH_TOKEN` to the same value as the Pi.
4. Run `python3 spotify_mac_watcher.py`.
5. Optional: install the LaunchAgent plist after replacing its placeholder paths.

## Behavior

- The Mac watcher polls Spotify every second.
- It waits 3 seconds for the selected track to settle before pushing.
- The watcher sends a lightweight heartbeat every 60 seconds. Heartbeats update connection freshness without refreshing the e-ink panel.
- If the Mac sleeps or disappears while Spotify still says it is playing, the Pi treats the last heartbeat time as the start of the idle period.
- The Pi only refreshes when visible playback state changes or an idle quote becomes due.
- When Spotify is paused or idle, the plugin can keep the last track, show its paused/nothing-playing screen, or show a motivational quote after a configurable delay.
- Quotes come from a local shuffled collection. Every quote is used before the collection is shuffled again, and the same quote is not shown twice in a row.
