# Template: How to Write check.py

Use this template to create the `check.py` validation script for any mission.

---

## Purpose

The check.py script:
1. **Validates** that students completed all required files
2. **Checks structure** (not correctness - that's Copilot's job)
3. **Provides feedback** celebrating skills proven
4. **Guides fixes** with helpful hints when something's missing

---

## Complete Template

```python
import json
from pathlib import Path
from typing import Optional

# ANSI Colors
GREEN = "\\033[92m"
RED = "\\033[91m"
YELLOW = "\\033[93m"
BLUE = "\\033[94m"
RESET = "\\033[0m"


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


def _write_copilot_input(path: Path, explain_text: str, mission_concept: str) -> None:
    """
    Generate copilot_input.txt with mission-specific rubric
    
    Args:
        path: Where to write copilot_input.txt
        explain_text: Content of explain.md
        mission_concept: e.g., "inheritance", "classes", "loops"
    """
    rubric = [
        f"- Part 1: Answered questions about different example (not the mission code)",
        f"- Part 2: Explained line-specific code with understanding",
        f"- Part 3: Comparison questions show deep thinking",
        f"- Part 4: Transfer challenge completed (new system designed)",
        f"- Part 5: Connected patterns back to mission code",
        f"- Shows understanding of {mission_concept}, not just memorization",
        f"- Uses plain language but demonstrates depth"
    ]
    
    prompt = [
        f"You are a strict grader helping a student learn {mission_concept}.",
        "Do not give the correct answer. Instead, ask probing questions to deepen understanding.",
        "",
        "Evaluate this explanation using the rubric:",
        *rubric,
        "",
        "For each item:",
        "- Score 0 (missing), 1 (partial), or 2 (complete)",
        "- If < 2, ask a question to guide deeper thinking",
        "- Example: 'You mentioned X but didn't explain WHY. Can you elaborate?'",
        "",
        "Here is the student's explanation:",
        "=" * 60,
        explain_text.strip(),
        "=" * 60,
    ]
    path.write_text("\\n".join(prompt), encoding="utf-8")


def print_completion_feedback(mission_name: str, core_concepts: list):
    """Print encouraging feedback highlighting skills proven"""
    print(f"\\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}MISSION COMPLETE: {mission_name}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}\\n")
    
    print("🎯 Skills You've Proven:\\n")
    for concept in core_concepts:
        print(f"  ✅ {concept}")
    
    print(f"\\n{BLUE}📊 What This Means:{RESET}")
    print("  • Not just 'it works' but 'I understand WHY and WHEN'")
    print("  • Ready to apply these patterns in new situations")
    print("  • Can explain concepts with concrete examples and metrics\\n")
    
    print(f"{BLUE}🔄 Next Steps:{RESET}")
    print("  1. Review your metrics from bad_code_explain.md")
    print("  2. What was your improvement ratio? Can you recall it?")
    print("  3. Try applying this pattern to a different domain\\n")


def print_helpful_hints(file_name: str, mission_specific_hints: dict):
    """Provide actionable guidance for incomplete files"""
    if file_name in mission_specific_hints:
        print(f"\\n  {YELLOW}Hints for {file_name}:{RESET}")
        for hint in mission_specific_hints[file_name]:
            print_hint(hint)


def check_mission():
    """Main check function for [MISSION_ID] [Mission Name]"""
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}[Mission Name] - Mission Verification{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\\n")
    
    all_passed = True

    # Find repo root
    repo_root = find_repo_root(Path.cwd())
    if not repo_root:
        print_result("Could not locate repo root (expected to find src/plugins).", False)
        print_hint("Run this inside the InkyPi repo, e.g. ~/InkyPi/academy/missions/[mission_folder]")
        return
    print_result(f"Repo root detected: {repo_root}", True)

    plugin_id = "[mission_id]"  # e.g., "c04_list_practice"
    plugin_dir = repo_root / "src" / "plugins" / plugin_id

    # ==================================================
    # PLUGIN FILE CHECKS
    # ==================================================
    
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
        
        # CUSTOMIZE: Check for mission-specific classes/functions
        py_content = python_file.read_text(encoding="utf-8")
        # Example: if "class BaseCard" in py_content and "class PetCard" in py_content:
        #   print_result("Python file contains required classes", True)
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
        print_hint("Temporary: cp src/plugins/clock/icon.png src/plugins/[mission_id]/")
        all_passed = False

    print(f"\\n{BLUE}--- Self-Learning Module Checks ---{RESET}\\n")

    mission_dir = Path(__file__).parent

    # ==================================================
    # SELF-LEARNING FILE CHECKS (CUSTOMIZE FOR MISSION)
    # ==================================================

    # Check explain.md
    explain_path = mission_dir / "explain.md"
    # CUSTOMIZE: Update keywords for your mission's different example
    # Example for C02: ["vehicle", "electric"] (not "creature")
    # Example for C04: ["shopping cart", "items"] (not "high scores")
    if _check_text_file(explain_path, 1000, keywords=[
        "[different_example_1]",  # e.g., "vehicle", "shopping cart"
        "[different_example_2]",  # e.g., "electric", "items"
        "line 13", "line 18",     # Line-specific questions
        "[transfer_concept_1]",   # e.g., "weapon", "book"
        "[transfer_concept_2]"    # e.g., "sword", "library"
    ]):
        print_result("explain.md: Different example with line-specific analysis ✓", True)
    else:
        print_result("explain.md: Missing, incomplete, or wrong format", False)
        print_helpful_hints("explain.md", {
            "explain.md": [
                "Remember: Use a DIFFERENT example (not the mission code)",
                "Answer line-specific questions (e.g., 'Line 13: ...')",
                "Complete the transfer challenge (design new system)",
                "Should have 22+ questions answered with specific details"
            ]
        })
        all_passed = False

    # Check debug_detective.md
    debug_detective_path = mission_dir / "debug_detective.md"
    # CUSTOMIZE: Update keywords for your mission's concepts
    if _check_text_file(debug_detective_path, 300, keywords=[
        "bug", "error", "fix", "[concept_keyword]"  # e.g., "super", "append", "index"
    ]):
        print_result("debug_detective.md: Debugging analysis completed ✓", True)
    else:
        print_result("debug_detective.md: Missing or incomplete", False)
        print_helpful_hints("debug_detective.md", {
            "debug_detective.md": [
                "Find all bugs in the broken code",
                "Explain WHY each is broken (connect to concepts)",
                "Show how you fixed them",
                "Predict what would break without the fixes"
            ]
        })
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
            print_helpful_hints("bad_code.py", {
                "bad_code.py": [
                    "Complete all 4 stages",
                    "Stage 2: Apply feature request to bad code",
                    "Stage 3: Refactor with [concept]",
                    "Stage 4: Compare - should be much easier!",
                    "File should be 500+ characters with working code"
                ]
            })
            all_passed = False
    else:
        print_result("bad_code.py: File missing", False)
        all_passed = False

    # Check bad_code_explain.md (5-part structure)
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
        print_helpful_hints("bad_code_explain.md", {
            "bad_code_explain.md": [
                "Part 1: Count exact lines changed (Stage 2 vs Stage 4)",
                "Part 2: Answer 'teammate adds...' questions",
                "Part 3: Second feature request predictions",
                "Part 4: When is [concept] overkill? (Rule of Three)",
                "Part 5: Real-world connections",
                "Should have 33 questions answered with specific metrics"
            ]
        })
        all_passed = False

    # Generate copilot_input.txt
    copilot_path = mission_dir / "copilot_input.txt"
    if explain_path.is_file() and explain_path.stat().st_size > 100:
        # CUSTOMIZE: Set mission concept (e.g., "inheritance", "lists", "functions")
        _write_copilot_input(copilot_path, explain_path.read_text(encoding="utf-8"), "[mission_concept]")
        print_result("copilot_input.txt generated ✓", True)
        print_hint("Use this with GitHub Copilot to grade your explain.md")
    else:
        print_result("copilot_input.txt not generated (explain.md missing/incomplete)", False)
        all_passed = False

    # ==================================================
    # FINAL SUMMARY
    # ==================================================
    
    print(f"\\n{BLUE}{'='*60}{RESET}")
    if all_passed:
        # CUSTOMIZE: Update mission name and core concepts
        print_completion_feedback(
            "[Mission Name]",
            [
                "[Concept 1] prevents [problem] (measured improvement ratio)",
                "[Concept 2] [benefit]",
                "Pattern recognition (transferred [Example A] to [Example B])",
                "Knowing when NOT to use [concept] (Rule of Three)",
                "Metrics-driven analysis (counted lines, compared approaches)"
            ]
        )
    else:
        print(f"{RED}MISSION NOT COMPLETE{RESET}")
        print(f"\\n{YELLOW}Review the hints above and complete missing items.{RESET}")
        print(f"{YELLOW}Then run 'python3 check.py' again.{RESET}\\n")


if __name__ == "__main__":
    check_mission()
```

---

## Customization Checklist

When creating check.py for a new mission, customize these sections:

### 1. Plugin ID and Names
- [ ] `plugin_id = "[mission_id]"` (e.g., "c04_list_practice")
- [ ] Mission name in header: `"[Mission Name] - Mission Verification"`
- [ ] Mission name in completion feedback

### 2. Python File Checks (Optional)
- [ ] Add class/function checks if needed:
  ```python
  if "class SomeClass" in py_content:
      print_result("Python file contains required classes", True)
  ```

### 3. explain.md Keywords
- [ ] Different example keywords (e.g., "vehicle", "shopping cart")
- [ ] Transfer challenge keywords (e.g., weapon", "book")

### 4. debug_detective.md Keywords
- [ ] Concept-specific keyword (e.g., "super", "append", "index")

### 5. Copilot Rubric
- [ ] Set `mission_concept` (e.g., "inheritance", "lists", "functions")

### 6. Completion Feedback
- [ ] Mission name
- [ ] 5 core concepts/skills specific to this mission
- [ ] Example: "Inheritance prevents code duplication (6:1 improvement ratio)"

### 7. Helpful Hints (Optional)
Customize hints in `print_helpful_hints()` for mission-specific guidance

---

## Example: C-03 Inheritance

See `/academy/missions/c03_inheritance_practice/check.py` for complete example.

**Customizations made**:
- plugin_id = "c03_inheritance_practice"
- explain.md keywords: "vehicle", "electric", "line 13", "weapon", "sword"
- debug_detective.md keywords: "bug", "error", "super"
- mission_concept = "inheritance and super()"
- 5 skills:
  - Inheritance prevents code duplication (6:1 ratio)
  - super() reuses parent methods
  - Pattern recognition (Vehicle → Weapon)
  - Knowing when not to (Rule of Three)
  - Metrics-driven analysis

---

## Validation Philosophy

**Don't check for**:
- ❌ Correctness of answers (Copilot's job)
- ❌ Exact wording
- ❌ Specific numerical values

**Do check for**:
- ✅ Structure is present (4 stages, 5 parts)
- ✅ Sufficient depth (character counts: 1000-1500)
- ✅ Key concepts mentioned (keywords)
- ✅ Student made genuine effort

**Goal**: Ensure engagement with exercises, not just skipping. Copilot grades understanding depth.
