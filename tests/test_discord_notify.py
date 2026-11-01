from datetime import datetime, timezone

from extras import discord_notify
from extras.discord_notify import build_notification, load_changes


def fields_named(message, prefix):
    fields = message["embeds"][0]["fields"]
    return [field for field in fields if field["name"].startswith(prefix)]


def combined_field_value(message, prefix):
    return "\n".join(field["value"] for field in fields_named(message, prefix))


def test_push_message_is_compact_and_lists_every_commit_and_file():
    commits = [
        {
            "id": "abc123456789",
            "message": "Clean up old plugins\n\nRemove practice copies.",
            "url": "https://github.com/DanielYcZhang/InkyPi/commit/abc1234",
        },
        {
            "id": "def567890123",
            "message": "Add better Discord updates",
            "url": "https://github.com/DanielYcZhang/InkyPi/commit/def5678",
        },
        {
            "id": "987abcd65432",
            "message": "Fix notifier tests",
            "url": "https://github.com/DanielYcZhang/InkyPi/commit/987abcd",
        },
    ]
    payload = {
        "ref": "refs/heads/develop",
        "compare": "https://github.com/DanielYcZhang/InkyPi/compare/old...new",
        "commits": commits,
        "head_commit": {**commits[-1], "timestamp": "2026-11-01T12:30:00+13:00"},
        "repository": {
            "full_name": "DanielYcZhang/InkyPi",
            "html_url": "https://github.com/DanielYcZhang/InkyPi",
        },
        "sender": {
            "login": "DanielYcZhang",
            "html_url": "https://github.com/DanielYcZhang",
        },
    }
    files = [
        {
            "filename": f"src/plugins/spotify/file_{index}.py",
            "status": "modified",
            "additions": index + 1,
            "deletions": index,
        }
        for index in range(14)
    ]
    changes = {"files": files, "additions": 105, "deletions": 91, "changed_files": 14}

    message = build_notification("push", payload, changes)

    embed = message["embeds"][0]
    assert embed["title"] == "[develop] 3 commits pushed"
    assert embed["description"] == (
        "[DanielYcZhang/InkyPi](https://github.com/DanielYcZhang/InkyPi)"
        " by [DanielYcZhang](https://github.com/DanielYcZhang)"
    )
    assert embed["url"] == payload["compare"]
    assert embed["timestamp"] == "2026-11-01T12:30:00+13:00"
    assert "author" not in embed
    assert [field["name"] for field in embed["fields"]][0] == "Changes"
    assert embed["fields"][0]["value"] == "14 files | +105 / -91"

    commit_text = combined_field_value(message, "Commits")
    for commit in commits:
        assert commit["id"][:7] in commit_text
        assert commit["message"].splitlines()[0] in commit_text

    file_text = combined_field_value(message, "Files")
    for file_data in files:
        assert file_data["filename"] in file_text

    repeated_names = {"Type", "Repository", "Author", "Branch", "Result", "Commit"}
    assert repeated_names.isdisjoint(field["name"] for field in embed["fields"])


def test_merged_pull_request_includes_body_commits_and_every_file():
    payload = {
        "action": "closed",
        "pull_request": {
            "number": 8,
            "title": "Clean up old plugins",
            "body": (
                "## What changed\n"
                "- Removed old practice plugins\n"
                "- Added better Discord updates\n\n"
                "## Testing\n"
                "- 91 tests passed"
            ),
            "html_url": "https://github.com/DanielYcZhang/InkyPi/pull/8",
            "merged": True,
            "merged_at": "2026-11-01T00:15:00Z",
            "changed_files": 15,
            "additions": 9,
            "deletions": 579,
            "head": {"ref": "develop", "sha": "1234567890"},
            "base": {"ref": "main"},
            "user": {
                "login": "DanielYcZhang",
                "html_url": "https://github.com/DanielYcZhang",
            },
        },
        "repository": {
            "full_name": "DanielYcZhang/InkyPi",
            "html_url": "https://github.com/DanielYcZhang/InkyPi",
        },
    }
    files = [
        {"filename": f"src/plugins/old_{index}.py", "status": "removed", "additions": 0, "deletions": 10}
        for index in range(15)
    ]
    commits = [
        {
            "sha": "1111111abcdef",
            "html_url": "https://github.com/DanielYcZhang/InkyPi/commit/1111111",
            "commit": {"message": "Clean up old plugins"},
        },
        {
            "sha": "2222222abcdef",
            "html_url": "https://github.com/DanielYcZhang/InkyPi/commit/2222222",
            "commit": {"message": "Add better Discord updates"},
        },
    ]
    changes = {
        "files": files,
        "commits": commits,
        "changed_files": 15,
        "additions": 9,
        "deletions": 579,
    }

    message = build_notification("pull_request", payload, changes)

    embed = message["embeds"][0]
    assert embed["title"] == "[main] PR #8 merged"
    assert "**Clean up old plugins**" in embed["description"]
    assert "**What changed**" in embed["description"]
    assert "Removed old practice plugins" in embed["description"]
    assert "**Testing**" in embed["description"]
    assert "91 tests passed" in embed["description"]
    assert "DanielYcZhang/InkyPi" in embed["description"]
    assert embed["timestamp"] == "2026-11-01T00:15:00Z"
    assert embed["fields"][0] == {
        "name": "Changes",
        "value": "15 files | +9 / -579",
        "inline": False,
    }
    assert "`develop` -> `main`" in embed["fields"][1]["value"]

    commit_text = combined_field_value(message, "Commits")
    assert "1111111" in commit_text
    assert "Clean up old plugins" in commit_text
    assert "2222222" in commit_text
    assert "Add better Discord updates" in commit_text

    file_text = combined_field_value(message, "Files")
    for file_data in files:
        assert file_data["filename"] in file_text


def test_fields_stay_within_discord_limits_and_explain_omissions():
    payload = {
        "ref": "refs/heads/main",
        "compare": "https://github.com/owner/repo/compare/old...new",
        "commits": [
            {
                "id": f"{index:07d}abcdef",
                "message": f"Update feature {index} with a useful but deliberately long explanation",
                "url": f"https://github.com/owner/repo/commit/{index}",
            }
            for index in range(120)
        ],
        "repository": {"full_name": "owner/repo", "html_url": "https://github.com/owner/repo"},
        "sender": {"login": "owner", "html_url": "https://github.com/owner"},
    }
    changes = {
        "files": [
            {
                "filename": f"src/a_very_long_directory_name/file_{index:03d}_with_details.py",
                "status": "modified",
                "additions": 10,
                "deletions": 2,
            }
            for index in range(120)
        ],
        "changed_files": 120,
        "additions": 1200,
        "deletions": 240,
    }

    message = build_notification("push", payload, changes)

    embed = message["embeds"][0]
    assert len(embed["fields"]) <= 25
    assert all(len(field["value"]) <= 1024 for field in embed["fields"])
    embed_character_count = len(embed["title"]) + len(embed.get("description", ""))
    embed_character_count += sum(len(field["name"]) + len(field["value"]) for field in embed["fields"])
    assert embed_character_count <= 6000
    assert "more commits" in combined_field_value(message, "Commits")
    assert "more files" in combined_field_value(message, "Files")


def test_load_changes_fetches_pull_request_files_and_commits(monkeypatch):
    urls = []

    def fake_get_json(url, token):
        urls.append(url)
        if "/files?" in url:
            return [{"filename": "src/app.py", "status": "modified"}]
        return [{"sha": "abc1234", "commit": {"message": "Fix app"}}]

    monkeypatch.setattr(discord_notify, "_get_json", fake_get_json)
    payload = {
        "repository": {"full_name": "owner/repo"},
        "pull_request": {
            "number": 12,
            "changed_files": 1,
            "additions": 4,
            "deletions": 2,
        },
    }

    changes = load_changes("pull_request", payload, "token", "https://api.github.test")

    assert changes["files"] == [{"filename": "src/app.py", "status": "modified"}]
    assert changes["commits"] == [{"sha": "abc1234", "commit": {"message": "Fix app"}}]
    assert urls == [
        "https://api.github.test/repos/owner/repo/pulls/12/files?per_page=100",
        "https://api.github.test/repos/owner/repo/pulls/12/commits?per_page=100",
    ]


def test_load_changes_fetches_every_pull_request_page(monkeypatch):
    urls = []

    def fake_get_json(url, token):
        urls.append(url)
        if "page=2" in url:
            return [{"filename": "last.py"}] if "/files?" in url else [{"sha": "last"}]
        prefix = "file" if "/files?" in url else "commit"
        return [{"filename": f"{prefix}-{index}.py"} for index in range(100)]

    monkeypatch.setattr(discord_notify, "_get_json", fake_get_json)
    payload = {
        "repository": {"full_name": "owner/repo"},
        "pull_request": {"number": 12, "changed_files": 101},
    }

    changes = load_changes("pull_request", payload, "token", "https://api.github.test")

    assert len(changes["files"]) == 101
    assert len(changes["commits"]) == 101
    assert urls == [
        "https://api.github.test/repos/owner/repo/pulls/12/files?per_page=100",
        "https://api.github.test/repos/owner/repo/pulls/12/files?per_page=100&page=2",
        "https://api.github.test/repos/owner/repo/pulls/12/commits?per_page=100",
        "https://api.github.test/repos/owner/repo/pulls/12/commits?per_page=100&page=2",
    ]


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
