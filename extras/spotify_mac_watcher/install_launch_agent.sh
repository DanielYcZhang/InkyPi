#!/bin/bash

set -euo pipefail

LABEL="com.inkypi.spotify-mac-watcher"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_PATH="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG_DIR="$HOME/Library/Logs/InkyPi"
LOG_PATH="$LOG_DIR/spotify-mac-watcher.log"
PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"
RUNNER_PATH="$SCRIPT_DIR/inkypi-spotify-watcher"

mkdir -p "$HOME/Library/LaunchAgents" "$LOG_DIR"

chmod +x "$RUNNER_PATH"

"$PYTHON_BIN" - "$PLIST_PATH" "$SCRIPT_DIR" "$LOG_PATH" "$RUNNER_PATH" "$PYTHON_BIN" <<'PY'
import plistlib
import sys
from pathlib import Path

plist_path, script_dir, log_path, runner_path, python_bin = sys.argv[1:]
config = {
    "Label": "com.inkypi.spotify-mac-watcher",
    "ProgramArguments": [runner_path],
    "WorkingDirectory": script_dir,
    "LimitLoadToSessionType": "Aqua",
    "ProcessType": "Background",
    "ThrottleInterval": 10,
    "RunAtLoad": True,
    "KeepAlive": True,
    "EnvironmentVariables": {
        "PYTHONUNBUFFERED": "1",
        "PYTHON_BIN": python_bin,
    },
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
launchctl print "gui/$UID/$LABEL" >/dev/null

echo "Installed and started $LABEL"
echo "Log: $LOG_PATH"

BTM_STATUS="$("$PYTHON_BIN" - "$LABEL" <<'PY'
import subprocess
import sys

try:
    result = subprocess.run(["sfltool", "dumpbtm"], capture_output=True, text=True, timeout=5)
    disposition = ""
    for line in result.stdout.splitlines():
        if "Disposition:" in line:
            disposition = line
        elif "Identifier:" in line and sys.argv[1] in line:
            print(disposition)
            break
except Exception:
    pass
PY
)"
if [[ "$BTM_STATUS" == *disallowed* ]]; then
    echo
    echo "WARNING: macOS is blocking this watcher from starting after login."
    echo "Open System Settings > General > Login Items & Extensions, then allow"
    echo "inkypi-spotify-watcher (or Unknown Developer) in Allow in Background."
elif [[ "$BTM_STATUS" != *allowed* ]]; then
    echo
    echo "Could not verify the macOS background permission."
    echo "Check System Settings > General > Login Items & Extensions and allow"
    echo "inkypi-spotify-watcher (or Unknown Developer) in Allow in Background."
fi
