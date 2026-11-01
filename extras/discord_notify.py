import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone


FILE_LIMIT = 10
DISCORD_FIELD_LIMIT = 1024
STATUS_LABELS = {
    "added": "A",
    "modified": "M",
    "removed": "D",
    "renamed": "R",
}


def _short_text(value, limit=180):
    text = (value or "").splitlines()[0].strip()
    if len(text) <= limit:
        return text
    return f"{text[: limit - 3].rstrip()}..."


def _link(label, url):
    return f"[{label}]({url})" if url else label


def _change_summary(changes):
    files = changes.get("changed_files", len(changes.get("files", [])))
    additions = changes.get("additions", 0)
    deletions = changes.get("deletions", 0)
    return f"{files} files | +{additions} / -{deletions}"


def _file_summary(files):
    lines = []
    shown = files[:FILE_LIMIT]
    for file_data in shown:
        status = STATUS_LABELS.get(file_data.get("status"), "?")
        filename = file_data.get("filename", "unknown file")
        additions = file_data.get("additions", 0)
        deletions = file_data.get("deletions", 0)
        lines.append(f"`{status}` {filename} (+{additions}/-{deletions})")

    remaining = len(files) - len(shown)
    if remaining:
        lines.append(f"...and {remaining} more files")

    value = "\n".join(lines) or "No file details available"
    if len(value) > DISCORD_FIELD_LIMIT:
        value = f"{value[: DISCORD_FIELD_LIMIT - 3].rstrip()}..."
    return value


def _base_fields(repository, author, event_type):
    return [
        {"name": "Type", "value": event_type, "inline": True},
        {
            "name": "Repository",
            "value": _link(repository.get("full_name", "Unknown"), repository.get("html_url")),
            "inline": True,
        },
        {
            "name": "Author",
            "value": _link(author.get("login", "Unknown"), author.get("html_url")),
            "inline": True,
        },
    ]


def _push_embed(payload, changes, now):
    repository = payload.get("repository", {})
    author = payload.get("sender", {})
    branch = payload.get("ref", "").removeprefix("refs/heads/") or "Unknown"
    commits = payload.get("commits", [])
    head_commit = payload.get("head_commit") or {}
    commit_count = len(commits)
    commit_label = "commit" if commit_count == 1 else "commits"
    title = f"[{branch}] {commit_count} new {commit_label}"
    sha = head_commit.get("id", "")
    commit_value = "No commit details available"
    if sha:
        commit_value = f"{_link(f'`{sha[:7]}`', head_commit.get('url'))} {_short_text(head_commit.get('message'))}"

    fields = _base_fields(repository, author, "Push")
    fields.extend(
        [
            {"name": "Branch", "value": f"`{branch}`", "inline": True},
            {"name": "Result", "value": "Pushed", "inline": True},
            {"name": "Changes", "value": _change_summary(changes), "inline": True},
            {"name": "Commit", "value": commit_value, "inline": False},
            {"name": "Files", "value": _file_summary(changes.get("files", [])), "inline": False},
        ]
    )
    return {
        "title": title,
        "url": payload.get("compare") or repository.get("html_url"),
        "color": 0x2F81F7,
        "author": {"name": author.get("login", "GitHub"), "icon_url": author.get("avatar_url", "")},
        "fields": fields,
        "timestamp": head_commit.get("timestamp") or now.isoformat(),
        "footer": {"text": "GitHub push"},
    }


def _pull_request_embed(payload, changes, now):
    repository = payload.get("repository", {})
    pull_request = payload.get("pull_request", {})
    author = pull_request.get("user", payload.get("sender", {}))
    action = payload.get("action", "updated")
    merged = bool(pull_request.get("merged"))
    result = "Merged" if merged else {
        "opened": "Opened",
        "reopened": "Reopened",
        "synchronize": "Updated",
        "ready_for_review": "Ready for review",
        "closed": "Closed",
    }.get(action, action.replace("_", " ").title())
    base_branch = pull_request.get("base", {}).get("ref", "Unknown")
    head_branch = pull_request.get("head", {}).get("ref", "Unknown")
    number = pull_request.get("number", "?")
    sha = pull_request.get("head", {}).get("sha", "")
    commit_url = f"{repository.get('html_url')}/commit/{sha}" if repository.get("html_url") and sha else None

    fields = _base_fields(repository, author, "Pull request")
    fields.extend(
        [
            {"name": "Branches", "value": f"`{head_branch}` -> `{base_branch}`", "inline": True},
            {"name": "Result", "value": result, "inline": True},
            {"name": "Changes", "value": _change_summary(changes), "inline": True},
            {"name": "Head commit", "value": _link(f"`{sha[:7]}`", commit_url) if sha else "Unknown", "inline": False},
            {"name": "Files", "value": _file_summary(changes.get("files", [])), "inline": False},
        ]
    )
    return {
        "title": f"[{base_branch}] PR #{number} {result.lower()}",
        "description": f"**{_short_text(pull_request.get('title'), 240)}**",
        "url": pull_request.get("html_url") or repository.get("html_url"),
        "color": 0x238636 if merged else 0xA371F7,
        "author": {"name": author.get("login", "GitHub"), "icon_url": author.get("avatar_url", "")},
        "fields": fields,
        "timestamp": pull_request.get("merged_at") or pull_request.get("updated_at") or now.isoformat(),
        "footer": {"text": "GitHub pull request"},
    }


def build_notification(event_name, payload, changes=None, now=None):
    now = now or datetime.now(timezone.utc)
    changes = changes or {}
    if event_name == "push":
        embed = _push_embed(payload, changes, now)
    elif event_name == "pull_request":
        embed = _pull_request_embed(payload, changes, now)
    else:
        raise ValueError(f"Unsupported GitHub event: {event_name}")
    return {"username": "InkyPi GitHub", "embeds": [embed]}


def _get_json(url, token):
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def load_changes(event_name, payload, token, api_url):
    repository = payload.get("repository", {}).get("full_name")
    if not repository or not token:
        return {}

    if event_name == "push":
        before = payload.get("before")
        after = payload.get("after")
        if not before or not after or set(before) == {"0"}:
            return {}
        data = _get_json(f"{api_url}/repos/{repository}/compare/{before}...{after}", token)
        files = data.get("files", [])
        return {
            "files": files,
            "changed_files": len(files),
            "additions": sum(file_data.get("additions", 0) for file_data in files),
            "deletions": sum(file_data.get("deletions", 0) for file_data in files),
        }

    pull_request = payload.get("pull_request", {})
    number = pull_request.get("number")
    files = _get_json(f"{api_url}/repos/{repository}/pulls/{number}/files?per_page=100", token) if number else []
    return {
        "files": files,
        "changed_files": pull_request.get("changed_files", len(files)),
        "additions": pull_request.get("additions", 0),
        "deletions": pull_request.get("deletions", 0),
    }


def send_notification(webhook_url, message):
    request = urllib.request.Request(
        webhook_url,
        data=json.dumps(message).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "InkyPi-GitHub-Notifier"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status not in (200, 204):
            raise RuntimeError(f"Discord returned HTTP {response.status}")


def main():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    event_name = os.environ.get("GITHUB_EVENT_NAME")
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not event_path or not event_name:
        raise SystemExit("GitHub event details are missing.")
    if not webhook_url:
        print("DISCORD_WEBHOOK_URL is not configured; skipping notification.")
        return

    with open(event_path, encoding="utf-8") as event_file:
        payload = json.load(event_file)

    token = os.environ.get("GITHUB_TOKEN", "")
    api_url = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    try:
        changes = load_changes(event_name, payload, token, api_url)
        send_notification(webhook_url, build_notification(event_name, payload, changes))
        print(f"Sent {event_name} update to Discord.")
    except (urllib.error.HTTPError, urllib.error.URLError) as error:
        raise SystemExit(f"Could not send Discord notification: {error}") from error


if __name__ == "__main__":
    main()
