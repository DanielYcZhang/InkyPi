#!/bin/bash

set -u

LABEL="com.inkypi.spotify-mac-watcher"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
STATE_PATH="$SCRIPT_DIR/spotify_mac_watcher_state.json"
ENV_PATH="$SCRIPT_DIR/.env"
DOMAIN="gui/$UID/$LABEL"

if launchctl print "$DOMAIN" >/dev/null 2>&1; then
    echo "Watcher: running"
else
    echo "Watcher: NOT RUNNING"
    echo "Repair: bash $SCRIPT_DIR/install_launch_agent.sh"
fi

BTM_STATUS="$(/usr/bin/python3 - "$LABEL" <<'PY'
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
    echo "Login startup: BLOCKED by macOS"
    echo "Allow inkypi-spotify-watcher (or Unknown Developer) in:"
    echo "System Settings > General > Login Items & Extensions > Allow in Background"
elif [[ "$BTM_STATUS" == *allowed* ]]; then
    echo "Login startup: allowed"
else
    echo "Login startup: UNKNOWN (macOS status check timed out)"
fi

if [[ -f "$STATE_PATH" ]]; then
    /usr/bin/python3 - "$STATE_PATH" <<'PY'
import json
import sys
from datetime import datetime

try:
    with open(sys.argv[1], encoding="utf-8") as state_file:
        state = json.load(state_file)
    posted_at = state.get("last_posted_at")
    posted_text = datetime.fromtimestamp(posted_at).astimezone().isoformat(timespec="seconds") if posted_at else "never"
    print(f"Last successful Pi update: {posted_text}")
    print(f"Last sent state: {state.get('last_sent_state') or 'unknown'}")
except Exception as exc:
    print(f"Watcher state: unreadable ({exc})")
PY
else
    echo "Last successful Pi update: never"
fi

PI_BASE_URL="$(sed -n 's/^PI_BASE_URL=//p' "$ENV_PATH" 2>/dev/null | tail -n 1)"
RESOLVED_BASE_URL="$(/usr/bin/python3 - "$STATE_PATH" 2>/dev/null <<'PY'
import json
import sys

try:
    with open(sys.argv[1], encoding="utf-8") as state_file:
        print(json.load(state_file).get("resolved_base_url") or "")
except Exception:
    pass
PY
)"

PI_REACHABLE=false
for base_url in "$PI_BASE_URL" "$RESOLVED_BASE_URL"; do
    if [[ -n "$base_url" ]] && curl -fsS --connect-timeout 3 --max-time 5 \
        "${base_url%/}/static/images/saved/spotify_now_playing.json" >/dev/null; then
        PI_REACHABLE=true
        break
    fi
done

if [[ "$PI_REACHABLE" == true ]]; then
    echo "Pi connection: reachable"
else
    echo "Pi connection: UNREACHABLE"
fi
