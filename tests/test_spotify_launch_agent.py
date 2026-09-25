import plistlib
from pathlib import Path


def test_launch_agent_is_configured_for_login_and_persistent_logs():
    plist_path = (
        Path(__file__).parents[1]
        / "extras"
        / "spotify_mac_watcher"
        / "com.inkypi.spotify-mac-watcher.plist"
    )
    with plist_path.open("rb") as plist_file:
        config = plistlib.load(plist_file)

    assert config["RunAtLoad"] is True
    assert config["KeepAlive"] is True
    assert config["LimitLoadToSessionType"] == "Aqua"
    assert config["ProgramArguments"][0] == "/usr/bin/python3"
    assert not config["StandardOutPath"].startswith("/tmp/")
    assert config["StandardErrorPath"] == config["StandardOutPath"]
