import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone


DISCORD_FIELD_LIMIT = 1024
DESCRIPTION_LIMIT = 1400
SECTION_VALUE_LIMIT = 800
MAX_SECTION_FIELDS = 2
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


def _truncate(value, limit):
    text = (value or "").strip()
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


def _summary_line(repository, author):
    repository_link = _link(repository.get("full_name", "Unknown"), repository.get("html_url"))
    author_link = _link(author.get("login", "Unknown"), author.get("html_url"))
    return f"{repository_link} by {author_link}"


def _section_fields(name, lines, source_url, item_name):
    if not lines:
        return [{"name": name, "value": f"No {item_name} details available", "inline": False}]

    chunks = []
    shown_count = 0
    for line in lines:
        candidate = f"{chunks[-1]}\n{line}" if chunks else line
        if chunks and len(candidate) <= SECTION_VALUE_LIMIT:
            chunks[-1] = candidate
            shown_count += 1
            continue
        if len(chunks) >= MAX_SECTION_FIELDS:
            break
        chunks.append(_truncate(line, SECTION_VALUE_LIMIT))
        shown_count += 1

    omitted = len(lines) - shown_count
    if omitted:
        suffix = f"...and {omitted} more {item_name}"
        if source_url:
            suffix += f" - [view all]({source_url})"
        while chunks and len(f"{chunks[-1]}\n{suffix}") > SECTION_VALUE_LIMIT:
            kept_lines = chunks[-1].splitlines()
            if len(kept_lines) == 1:
                break
            kept_lines.pop()
            shown_count -= 1
            omitted += 1
            suffix = f"...and {omitted} more {item_name}"
            if source_url:
                suffix += f" - [view all]({source_url})"
            chunks[-1] = "\n".join(kept_lines)
        chunks[-1] = f"{chunks[-1]}\n{suffix}"

    total = len(chunks)
    return [
        {
            "name": name if total == 1 else f"{name} ({index}/{total})",
            "value": _truncate(chunk, DISCORD_FIELD_LIMIT),
            "inline": False,
        }
        for index, chunk in enumerate(chunks, start=1)
    ]


def _commit_lines(commits):
    lines = []
    for commit in commits:
        sha = commit.get("id") or commit.get("sha") or ""
        details = commit.get("commit", {})
        message = commit.get("message") or details.get("message") or "No commit message"
        url = commit.get("url") or commit.get("html_url")
        label = _link(f"`{sha[:7]}`", url) if sha else "`unknown`"
        lines.append(f"{label} {_short_text(message, 120)}")
    return lines


def _file_lines(files):
    lines = []
    for file_data in files:
        status = STATUS_LABELS.get(file_data.get("status"), "?")
        filename = file_data.get("filename", "unknown file")
        additions = file_data.get("additions", 0)
        deletions = file_data.get("deletions", 0)
        lines.append(f"`{status}` {filename} (+{additions}/-{deletions})")
    return lines


def _format_pull_request_body(body):
    lines = []
    for line in (body or "").strip().splitlines():
        if line.startswith("### "):
            line = f"**{line[4:]}**"
        elif line.startswith("## "):
            line = f"**{line[3:]}**"
        lines.append(line)
    return "\n".join(lines)


def _push_embed(payload, changes, now):
    repository = payload.get("repository", {})
    author = payload.get("sender", {})
    branch = payload.get("ref", "").removeprefix("refs/heads/") or "Unknown"
    commits = payload.get("commits", [])
    head_commit = payload.get("head_commit") or {}
    commit_count = len(commits)
    commit_label = "commit" if commit_count == 1 else "commits"
    title = f"[{branch}] {commit_count} {commit_label} pushed"
    compare_url = payload.get("compare") or repository.get("html_url")
    fields = [{"name": "Changes", "value": _change_summary(changes), "inline": False}]
    fields.extend(_section_fields("Commits", _commit_lines(commits), compare_url, "commits"))
    fields.extend(_section_fields("Files", _file_lines(changes.get("files", [])), compare_url, "files"))
    return {
        "title": title,
        "description": _summary_line(repository, author),
        "url": compare_url,
        "color": 0x2F81F7,
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
    pull_request_url = pull_request.get("html_url") or repository.get("html_url")
    body = _format_pull_request_body(pull_request.get("body"))
    description_parts = [
        _summary_line(repository, author),
        f"**{_short_text(pull_request.get('title'), 240)}**",
    ]
    if body:
        description_parts.append(body)

    fields = [
        {"name": "Changes", "value": _change_summary(changes), "inline": False},
        {"name": "Branches", "value": f"`{head_branch}` -> `{base_branch}`", "inline": False},
    ]
    fields.extend(_section_fields("Commits", _commit_lines(changes.get("commits", [])), pull_request_url, "commits"))
    fields.extend(_section_fields("Files", _file_lines(changes.get("files", [])), pull_request_url, "files"))
    return {
        "title": f"[{base_branch}] PR #{number} {result.lower()}",
        "description": _truncate("\n\n".join(description_parts), DESCRIPTION_LIMIT),
        "url": pull_request_url,
        "color": 0x238636 if merged else 0xA371F7,
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


def _get_all_pages(url, token):
    items = []
    page = 1
    while True:
        page_url = url if page == 1 else f"{url}&page={page}"
        batch = _get_json(page_url, token)
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


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
    files = _get_all_pages(f"{api_url}/repos/{repository}/pulls/{number}/files?per_page=100", token) if number else []
    commits = _get_all_pages(f"{api_url}/repos/{repository}/pulls/{number}/commits?per_page=100", token) if number else []
    return {
        "files": files,
        "commits": commits,
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
