import json
from pathlib import Path
from typing import Optional

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def print_result(msg, success):
    if success:
        print(f"[{GREEN}PASS{RESET}] {msg}")
    else:
        print(f"[{RED}FAIL{RESET}] {msg}")


def find_repo_root(start_dir: Path) -> Optional[Path]:
    current = start_dir.resolve()
    for _ in range(8):
        if (current / "src" / "plugins").is_dir():
            return current
        current = current.parent
    return None


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _check_text_file(path: Path, min_chars: int, keywords=None) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    if len(text.strip()) < min_chars:
        return False
    if keywords:
        lowered = text.lower()
        return all(k.lower() in lowered for k in keywords)
    return True


def _write_copilot_input(path: Path, explain_text: str) -> None:
    rubric = [
        "- Mentions class vs object correctly",
        "- Mentions properties stored with self",
        "- Describes what changes on the screen",
        "- Uses plain language suitable for a 12-year-old",
    ]
    prompt = [
        "You are a strict grader. Do not give the correct answer.",
        "Evaluate my explanation using this rubric:",
        *rubric,
        "",
        "Score each item 0-2 and explain what is missing.",
        "",
        "Here is my explanation:",
        explain_text.strip(),
        "",
    ]
    path.write_text("\n".join(prompt), encoding="utf-8")


def check_mission():
    print("Initiating Creature Card Verification...\n")
    all_passed = True

    repo_root = find_repo_root(Path.cwd())
    if not repo_root:
        print_result("Could not locate repo root (expected to find src/plugins).", False)
        print("  -> Hint: run this inside the InkyPi repo, e.g. ~/InkyPi/academy/missions/c02_creature_card")
        return
    print_result(f"Repo root detected: {repo_root}", True)

    plugin_id = "c02_creature_card"
    plugin_dir = repo_root / "src" / "plugins" / plugin_id

    if plugin_dir.is_dir():
        print_result(f"Plugin folder exists: src/plugins/{plugin_id}", True)
    else:
        print_result(f"Missing plugin folder: src/plugins/{plugin_id}", False)
        all_passed = False

    plugin_info_path = plugin_dir / "plugin-info.json"
    if plugin_info_path.is_file():
        try:
            plugin_info = _read_json(plugin_info_path)
            print_result("plugin-info.json is valid JSON", True)
        except Exception as e:
            print_result(f"plugin-info.json is not valid JSON: {e}", False)
            all_passed = False
            plugin_info = {}
    else:
        print_result("Missing file: plugin-info.json", False)
        all_passed = False
        plugin_info = {}

    if plugin_info.get("id") == plugin_id:
        print_result(f"Plugin id matches folder name: {plugin_id}", True)
    else:
        print_result(f"Plugin id mismatch: expected '{plugin_id}', found '{plugin_info.get('id')}'", False)
        all_passed = False

    python_file = plugin_dir / f"{plugin_id}.py"
    if python_file.is_file():
        print_result(f"Python file exists: {python_file.name}", True)
    else:
        print_result(f"Missing python file: {python_file.name}", False)
        all_passed = False

    icon_path = plugin_dir / "icon.png"
    if icon_path.is_file():
        print_result("Icon exists: icon.png", True)
    else:
        print_result("Missing icon.png", False)
        all_passed = False

    mission_dir = Path(__file__).parent
    explain_path = mission_dir / "explain.md"
    if _check_text_file(explain_path, 200, keywords=["class", "object", "self"]):
        print_result("explain.md completed", True)
    else:
        print_result("explain.md missing or incomplete", False)
        all_passed = False

    if _check_text_file(mission_dir / "predict.md", 80):
        print_result("predict.md completed", True)
    else:
        print_result("predict.md missing or incomplete", False)
        all_passed = False

    if _check_text_file(mission_dir / "trace.md", 60):
        print_result("trace.md completed", True)
    else:
        print_result("trace.md missing or incomplete", False)
        all_passed = False

    bad_code_py = mission_dir / "bad_code.py"
    if _check_text_file(bad_code_py, 120, keywords=["class Creature"]):
        print_result("bad_code.py present", True)
    else:
        print_result("bad_code.py missing or incomplete", False)
        all_passed = False

    if _check_text_file(mission_dir / "bad_code_explain.md", 80, keywords=["why"]):
        print_result("bad_code_explain.md completed", True)
    else:
        print_result("bad_code_explain.md missing or incomplete", False)
        all_passed = False

    copilot_path = mission_dir / "copilot_input.txt"
    if explain_path.is_file():
        _write_copilot_input(copilot_path, explain_path.read_text(encoding="utf-8"))
        print_result("copilot_input.txt generated", True)
    else:
        print_result("copilot_input.txt not generated (missing explain.md)", False)
        all_passed = False

    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. Your creature is ready.{RESET}")
    else:
        print(f"{RED}MISSION FAILED. Missing requirements.{RESET}")


if __name__ == "__main__":
    check_mission()
