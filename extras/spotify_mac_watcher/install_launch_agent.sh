#!/bin/bash

set -euo pipefail

LABEL="com.inkypi.spotify-mac-watcher"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_PATH="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG_DIR="$HOME/Library/Logs/InkyPi"
LOG_PATH="$LOG_DIR/spotify-mac-watcher.log"
PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"

mkdir -p "$HOME/Library/LaunchAgents" "$LOG_DIR"

"$PYTHON_BIN" - "$PLIST_PATH" "$SCRIPT_DIR" "$LOG_PATH" "$PYTHON_BIN" <<'PY'
import plistlib
import sys
from pathlib import Path

plist_path, script_dir, log_path, python_bin = sys.argv[1:]
config = {
    "Label": "com.inkypi.spotify-mac-watcher",
    "ProgramArguments": [python_bin, str(Path(script_dir) / "spotify_mac_watcher.py")],
    "WorkingDirectory": script_dir,
    "LimitLoadToSessionType": "Aqua",
    "ProcessType": "Background",
    "ThrottleInterval": 10,
    "RunAtLoad": True,
    "KeepAlive": True,
    "StandardOutPath": log_path,
    "StandardErrorPath": log_path,
}
with open(plist_path, "wb") as plist_file:
    plistlib.dump(config, plist_file)
PY

plutil -lint "$PLIST_PATH"
launchctl bootout "gui/$UID/$LABEL" >/dev/null 2>&1 || true
launchctl enable "gui/$UID/$LABEL"
launchctl bootstrap "gui/$UID" "$PLIST_PATH"
launchctl kickstart -k "gui/$UID/$LABEL"

echo "Installed and started $LABEL"
echo "Log: $LOG_PATH"
