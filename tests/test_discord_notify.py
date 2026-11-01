from datetime import datetime, timezone

from extras.discord_notify import build_notification


def field_value(message, name):
    fields = message["embeds"][0]["fields"]
    return next(field["value"] for field in fields if field["name"] == name)


def test_builds_detailed_push_message():
    payload = {
        "ref": "refs/heads/develop",
        "compare": "https://github.com/DanielYcZhang/InkyPi/compare/old...new",
        "commits": [{"id": "abc1234"}, {"id": "def5678"}],
        "head_commit": {
            "id": "def567890123",
            "message": "Update quotes\n\nExtra details",
            "url": "https://github.com/DanielYcZhang/InkyPi/commit/def5678",
            "timestamp": "2026-11-01T12:30:00+13:00",
        },
        "repository": {
            "full_name": "DanielYcZhang/InkyPi",
            "html_url": "https://github.com/DanielYcZhang/InkyPi",
        },
        "sender": {
            "login": "DanielYcZhang",
            "html_url": "https://github.com/DanielYcZhang",
            "avatar_url": "https://example.com/avatar.png",
        },
    }
    changes = {
        "files": [
            {"filename": "src/plugins/spotify/quotes.py", "status": "modified", "additions": 8, "deletions": 3},
            {"filename": "tests/test_quotes.py", "status": "added", "additions": 20, "deletions": 0},
        ],
        "additions": 28,
        "deletions": 3,
        "changed_files": 2,
    }

    message = build_notification("push", payload, changes)

    embed = message["embeds"][0]
    assert embed["title"] == "[develop] 2 new commits"
    assert embed["url"] == payload["compare"]
    assert embed["timestamp"] == "2026-11-01T12:30:00+13:00"
    assert field_value(message, "Repository") == "[DanielYcZhang/InkyPi](https://github.com/DanielYcZhang/InkyPi)"
    assert field_value(message, "Author") == "[DanielYcZhang](https://github.com/DanielYcZhang)"
    assert field_value(message, "Commit") == "[`def5678`](https://github.com/DanielYcZhang/InkyPi/commit/def5678) Update quotes"
    assert field_value(message, "Result") == "Pushed"
    assert field_value(message, "Changes") == "2 files | +28 / -3"
    assert "`M` src/plugins/spotify/quotes.py (+8/-3)" in field_value(message, "Files")


def test_builds_merged_pull_request_message():
    payload = {
        "action": "closed",
        "pull_request": {
            "number": 8,
            "title": "Clean up old plugins",
            "html_url": "https://github.com/DanielYcZhang/InkyPi/pull/8",
            "merged": True,
            "merged_at": "2026-11-01T00:15:00Z",
            "changed_files": 17,
            "additions": 9,
            "deletions": 579,
            "head": {"ref": "develop", "sha": "1234567890"},
            "base": {"ref": "main"},
            "user": {
                "login": "DanielYcZhang",
                "html_url": "https://github.com/DanielYcZhang",
                "avatar_url": "https://example.com/avatar.png",
            },
        },
        "repository": {
            "full_name": "DanielYcZhang/InkyPi",
            "html_url": "https://github.com/DanielYcZhang/InkyPi",
        },
    }
    changes = {
        "files": [{"filename": f"src/plugins/old_{index}.py", "status": "removed", "additions": 0, "deletions": 10} for index in range(15)],
        "changed_files": 17,
        "additions": 9,
        "deletions": 579,
    }

    message = build_notification("pull_request", payload, changes)

    embed = message["embeds"][0]
    assert embed["title"] == "[main] PR #8 merged"
    assert embed["description"] == "**Clean up old plugins**"
    assert embed["timestamp"] == "2026-11-01T00:15:00Z"
    assert field_value(message, "Branches") == "`develop` -> `main`"
    assert field_value(message, "Result") == "Merged"
    assert field_value(message, "Changes") == "17 files | +9 / -579"
    assert "...and 5 more files" in field_value(message, "Files")


def test_message_uses_current_time_when_event_has_no_timestamp():
    payload = {
        "ref": "refs/heads/main",
        "commits": [],
        "repository": {"full_name": "owner/repo", "html_url": "https://github.com/owner/repo"},
        "sender": {"login": "owner", "html_url": "https://github.com/owner"},
    }
    now = datetime(2026, 11, 1, 1, 2, 3, tzinfo=timezone.utc)

    message = build_notification("push", payload, {}, now=now)

    assert message["embeds"][0]["timestamp"] == "2026-11-01T01:02:03+00:00"
