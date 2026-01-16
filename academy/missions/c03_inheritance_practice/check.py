import json
from pathlib import Path
from typing import Optional

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def print_result(msg, success):
    """Print check result with color"""
    if success:
        print(f"[{GREEN}PASS{RESET}] {msg}")
    else:
        print(f"[{RED}FAIL{RESET}] {msg}")


def print_hint(msg):
    """Print helpful hint in yellow"""
    print(f"  {YELLOW}→{RESET} {msg}")


def find_repo_root(start_dir: Path) -> Optional[Path]:
    """Find InkyPi repo root by looking for src/plugins"""
    current = start_dir.resolve()
    for _ in range(8):
        if (current / "src" / "plugins").is_dir():
            return current
        current = current.parent
    return None


def _read_json(path: Path) -> dict:
    """Read and parse JSON file"""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _check_text_file(path: Path, min_chars: int, keywords=None) -> bool:
    """
    Check if text file exists, has minimum content, and contains keywords
    
    Args:
        path: Path to file
        min_chars: Minimum character count
        keywords: Optional list of keywords that must appear
    
    Returns:
        True if all checks pass
    """
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
    """
    Generate copilot_input.txt with mission-specific rubric
    
    Args:
        path: Where to write copilot_input.txt
        explain_text: Content of explain.md
    """
    rubric = [
        "- Part 1: Answered questions about Vehicle/ElectricCar example (different from cards)",
        "- Part 2: Explained line-specific code (Line 13, 18, etc.) with understanding",
        "- Part 3: Comparison questions show deep thinking about inheritance",
        "- Part 4: Transfer challenge completed (Weapon/Sword/Bow system designed)",
        "- Part 5: Connected patterns back to C-03 mission code",
        "- Shows understanding of inheritance and super(), not just memorization",
        "- Uses plain language but demonstrates depth"
    ]
    
    prompt = [
        "You are a strict grader helping a student learn inheritance and super().",
        "Do not give the correct answer. Instead, ask probing questions to deepen understanding.",
        "",
        "Evaluate this explanation using the rubric:",
        *rubric,
        "",
        "For each item:",
        "- Score 0 (missing), 1 (partial), or 2 (complete)",
        "- If < 2, ask a question to guide deeper thinking",
        "- Example: 'You mentioned super() but didn't explain WHY it prevents duplication. Can you elaborate?'",
        "",
        "Here is the student's explanation:",
        "=" * 60,
        explain_text.strip(),
        "=" * 60,
    ]
    path.write_text("\n".join(prompt), encoding="utf-8")


def print_completion_feedback():
    """Print encouraging feedback highlighting skills proven"""
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}MISSION COMPLETE: Inheritance Practice{RESET}")
    print(f"{GREEN}{'='*60}{RESET}\n")
    
    print("🎯 Skills You've Proven:\n")
    concepts = [
        "Inheritance prevents code duplication (measured improvement ratio)",
        "super() reuses parent methods without copy-paste",
        "Pattern recognition (transferred Vehicle to Weapon systems)",
        "Knowing when NOT to use inheritance (Rule of Three)",
        "Metrics-driven analysis (counted lines, compared approaches)"
    ]
    for concept in concepts:
        print(f"  ✅ {concept}")
    
    print(f"\n{BLUE}📊 What This Means:{RESET}")
    print("  • Not just 'it works' but 'I understand WHY and WHEN'")
    print("  • Ready to apply inheritance patterns in new situations")
    print("  • Can explain concepts with concrete examples and metrics\n")
    
    print(f"{BLUE}🔄 Next Steps:{RESET}")
    print("  1. Review your metrics from bad_code_explain.md")
    print("  2. What was your improvement ratio? Can you recall it?")
    print("  3. Try designing a game character hierarchy (BaseCharacter → Warrior/Mage/Rogue)\n")


def print_helpful_hints(file_name: str):
    """Provide actionable guidance for incomplete files"""
    hints = {
        "explain.md": [
            "Remember: Use the Vehicle/ElectricCar example (different from cards)",
            "Answer line-specific questions (e.g., 'Line 13: What does super().__init__() do?')",
            "Complete the transfer challenge (design Weapon/Sword/Bow system)",
            "Should have 22+ questions answered with specific details"
        ],
        "debug_detective.md": [
            "Find all 3 bugs in the broken code",
            "Explain WHY each is broken (connect to inheritance concepts)",
            "Show how you fixed them with proper super() usage",
            "Predict what would break without the fixes"
        ],
        "bad_code.py": [
            "Complete all 4 stages (check for comments: STAGE 1, 2, 3, 4)",
            "Stage 2: Add subtitle to bad code (without inheritance)",
            "Stage 3: Refactor with BaseCard + inheritance",
            "Stage 4: Compare - should be much easier!",
            "File should be 500+ characters with working code"
        ],
        "bad_code_explain.md": [
            "Part 1: Count exact lines changed (Stage 2 vs Stage 4)",
            "Part 2: Answer 'teammate adds AchievementCard' questions",
            "Part 3: Second feature request predictions",
            "Part 4: When is inheritance overkill? (Rule of Three)",
            "Part 5: Real-world connections (mobile games, 50 cards)",
            "Should have 33 questions answered with specific metrics"
        ]
    }
    
    if file_name in hints:
        print(f"\n  {YELLOW}Hints for {file_name}:{RESET}")
        for hint in hints[file_name]:
            print_hint(hint)


def check_mission():
    """Main check function for C-03 Inheritance Practice"""
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Inheritance Practice - Mission Verification{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    all_passed = True

    # Find repo root
    repo_root = find_repo_root(Path.cwd())
    if not repo_root:
        print_result("Could not locate repo root (expected to find src/plugins).", False)
        print_hint("Run this inside the InkyPi repo, e.g. ~/InkyPi/academy/missions/c03_inheritance_practice")
        return
    print_result(f"Repo root detected: {repo_root}", True)

    plugin_id = "c03_inheritance_practice"
    plugin_dir = repo_root / "src" / "plugins" / plugin_id

    # Check plugin folder
    if plugin_dir.is_dir():
        print_result(f"Plugin folder exists: src/plugins/{plugin_id}", True)
    else:
        print_result(f"Missing plugin folder: src/plugins/{plugin_id}", False)
        print_hint(f"Run: mkdir -p src/plugins/{plugin_id}")
        all_passed = False

    # Check plugin-info.json
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
        print_hint("Create plugin-info.json with id, display_name, and class fields")
        all_passed = False
        plugin_info = {}

    # Check plugin ID matches
    if plugin_info.get("id") == plugin_id:
        print_result(f"Plugin id matches folder name: {plugin_id}", True)
    else:
        print_result(f"Plugin id mismatch: expected '{plugin_id}', found '{plugin_info.get('id')}'", False)
        all_passed = False

    # Check Python file
    python_file = plugin_dir / f"{plugin_id}.py"
    if python_file.is_file():
        print_result(f"Python file exists: {python_file.name}", True)
        
        # Check for BaseCard and PetCard classes
        py_content = python_file.read_text(encoding="utf-8")
        if "class BaseCard" in py_content and "class PetCard" in py_content:
            print_result("Python file contains BaseCard and PetCard classes", True)
        else:
            print_result("Python file missing BaseCard or PetCard classes", False)
            all_passed = False
    else:
        print_result(f"Missing python file: {python_file.name}", False)
        print_hint(f"Copy template: cp academy/missions/{plugin_id}/{plugin_id}.py src/plugins/{plugin_id}/")
        all_passed = False

    # Check icon
    icon_path = plugin_dir / "icon.png"
    if icon_path.is_file():
        print_result("Icon exists: icon.png", True)
    else:
        print_result("Missing icon.png", False)
        print_hint("Temporary: cp src/plugins/clock/icon.png src/plugins/c03_inheritance_practice/")
        all_passed = False

    print(f"\n{BLUE}--- Self-Learning Module Checks ---{RESET}\n")

    mission_dir = Path(__file__).parent

    # Check explain.md (enhanced validation)
    explain_path = mission_dir / "explain.md"
    if _check_text_file(explain_path, 1000, keywords=[
        "vehicle", "electric",      # Different example (not cards)
        "line 13", "line 18",       # Line-specific questions
        "weapon", "sword"           # Transfer challenge
    ]):
        print_result("explain.md: Vehicle example with line-specific analysis ✓", True)
    else:
        print_result("explain.md: Missing, incomplete, or wrong format", False)
        print_helpful_hints("explain.md")
        all_passed = False

    # Check debug_detective.md (replaces predict.md and trace.md)
    debug_detective_path = mission_dir / "debug_detective.md"
    if _check_text_file(debug_detective_path, 300, keywords=[
        "bug", "error", "fix", "super"
    ]):
        print_result("debug_detective.md: Debugging analysis completed ✓", True)
    else:
        print_result("debug_detective.md: Missing or incomplete", False)
        print_helpful_hints("debug_detective.md")
        all_passed = False

    # Check bad_code.py (4-stage structure)
    bad_code_py = mission_dir / "bad_code.py"
    if bad_code_py.is_file():
        bad_code_text = bad_code_py.read_text(encoding="utf-8")
        has_all_stages = all([
            "Stage 1" in bad_code_text or "STAGE 1" in bad_code_text,
            "Stage 2" in bad_code_text or "STAGE 2" in bad_code_text,
            "Stage 3" in bad_code_text or "STAGE 3" in bad_code_text,
            "Stage 4" in bad_code_text or "STAGE 4" in bad_code_text
        ])
        
        if has_all_stages and len(bad_code_text) >= 500:
            print_result("bad_code.py: All 4 stages present ✓", True)
        else:
            print_result("bad_code.py: Missing stages or too short", False)
            print_helpful_hints("bad_code.py")
            all_passed = False
    else:
        print_result("bad_code.py: File missing", False)
        all_passed = False

    # Check bad_code_explain.md (5-part structure with metrics)
    bad_code_explain_path = mission_dir / "bad_code_explain.md"
    if _check_text_file(bad_code_explain_path, 1500, keywords=[
        "lines changed",        # Part 1: Metrics
        "teammate",            # Part 2: Team collaboration
        "improvement ratio",   # Part 3: Scalability
        "rule of three",       # Part 4: When not to use
        "real-world"           # Part 5: Connection
    ]):
        print_result("bad_code_explain.md: 5-part analysis with metrics ✓", True)
    else:
        print_result("bad_code_explain.md: Missing, incomplete, or lacks depth", False)
        print_helpful_hints("bad_code_explain.md")
        all_passed = False

    # Generate copilot_input.txt
    copilot_path = mission_dir / "copilot_input.txt"
    if explain_path.is_file() and explain_path.stat().st_size > 100:
        _write_copilot_input(copilot_path, explain_path.read_text(encoding="utf-8"))
        print_result("copilot_input.txt generated ✓", True)
        print_hint("Use this with GitHub Copilot to grade your explain.md")
    else:
        print_result("copilot_input.txt not generated (explain.md missing/incomplete)", False)
        all_passed = False

    # Final summary
    print(f"\n{BLUE}{'='*60}{RESET}")
    if all_passed:
        print_completion_feedback()
    else:
        print(f"{RED}MISSION NOT COMPLETE{RESET}")
        print(f"\n{YELLOW}Review the hints above and complete missing items.{RESET}")
        print(f"{YELLOW}Then run 'python3 check.py' again.{RESET}\n")


if __name__ == "__main__":
    check_mission()
