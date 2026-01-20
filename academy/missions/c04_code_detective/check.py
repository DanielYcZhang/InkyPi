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


def print_completion_feedback():
    """Print encouraging feedback highlighting skills proven"""
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}MISSION COMPLETE: The Code Detective{RESET}")
    print(f"{GREEN}{'='*60}{RESET}\n")
    
    print("🎯 Skills You've Proven:\n")
    concepts = [
        "Code Reading: Traced execution flow from web UI to display",
        "Architecture Understanding: Grasped BasePlugin contract pattern",
        "System Thinking: Created complete architecture diagram",
        "Interface Recognition: Identified required vs optional methods",
        "Debugging Readiness: Know where to look when things break"
    ]
    for concept in concepts:
        print(f"  ✅ {concept}")
    
    print(f"\n{BLUE}📊 What This Means:{RESET}")
    print("  • Not just 'write code' but 'READ and UNDERSTAND code'")
    print("  • Ready to navigate ANY codebase systematically")
    print("  • Can explain system architecture to others")
    print("  • Stack traces make sense (you recognize file names)\n")
    
    print(f"{BLUE}🔄 Next Steps:{RESET}")
    print("  1. Keep your architecture diagram - reference it when debugging!")
    print("  2. Practice reading code in other projects (Flask, Django, etc.)")
    print("  3. Next mission (M-08): Apply this knowledge building anime gallery\n")


def print_helpful_hints(file_name: str, missing_section: str = None):
    """Provide actionable guidance for incomplete files"""
    hints = {
        "c04_architecture.md": [
            "→ Must include architecture diagram (ASCII art or description)",
            "→ Answer all 5 detective questions from checkpoints",
            "→ Document 3 'Aha!' moments with before/after",
            "→ Complete debugging scenarios with specific file/module references"
        ],
        "explain.md": [
            "→ Explain Flask app (different example, not InkyPi)",
            "→ Answer line-specific questions (Line 4, 7, 13, 14, 18)",
            "→ Complete comparison questions (Flask vs InkyPi architecture)",
            "→ Design blog API system (transfer challenge)"
        ],
        "debug_detective.md": [
            "→ Predict all 3 bugs before running code",
            "→ Explain WHY each bug breaks (not just 'it's wrong')",
            "→ Connect each bug to architecture concepts",
            "→ Relate fixes back to InkyPi's approach"
        ],
        "bad_code.py": [
            "→ File should have all 4 stages marked",
            "→ Stage 2: Add custom_message parameter",
            "→ Stage 3: Refactor with BaseNotification class",
            "→ Stage 4: Add timestamp (shows architecture advantage)"
        ],
        "bad_code_explain.md": [
            "→ Part 1: Calculate exact improvement ratios with numbers",
            "→ Part 2: Answer team collaboration scenarios",
            "→ Part 3: Predict second feature request changes",
            "→ Part 4: Apply 'Rule of Three' with reasoning",
            "→ Part 5: Connect to real-world (InkyPi, Spotify, games)"
        ]
    }
    
    if file_name in hints:
        print(f"\n  {YELLOW}Hints for {file_name}:{RESET}")
        for hint in hints[file_name]:
            print_hint(hint)
        
        if missing_section:
            print(f"\n  {YELLOW}Missing section: {missing_section}{RESET}")


def check_mission():
    """Main check function for C-04 Code Detective"""
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}The Code Detective - Mission Verification{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    all_passed = True
    mission_dir = Path(__file__).parent

    # ==================================================
    # ARCHITECTURE DELIVERABLE CHECK (Main Output)
    # ==================================================
    
    print(f"{BLUE}--- Main Deliverable ---{RESET}\n")
    
    architecture_path = mission_dir / "c04_architecture.md"
    if architecture_path.is_file():
        content = architecture_path.read_text(encoding="utf-8")
        
        # Check for required sections
        has_diagram = any([
            "diagram" in content.lower(),
            "→" in content or "↓" in content,  # ASCII art arrows
            "web ui" in content.lower() and "display" in content.lower()
        ])
        
        has_questions = all([
            "checkpoint 1" in content.lower(),
            "checkpoint 2" in content.lower(),
            "checkpoint 3" in content.lower(),
            "checkpoint 4" in content.lower()
        ])
        
        has_aha_moments = "aha" in content.lower() and len(content) > 2000
        
        has_debugging = "scenario" in content.lower() or "debug" in content.lower()
        
        if has_diagram and has_questions and has_aha_moments and has_debugging:
            print_result("c04_architecture.md: Complete with diagram + questions + insights ✓", True)
        else:
            print_result("c04_architecture.md: Missing required sections", False)
            if not has_diagram:
                print_helpful_hints("c04_architecture.md", "Architecture diagram")
            if not has_questions:
                print_helpful_hints("c04_architecture.md", "Detective questions from checkpoints")
            if not has_aha_moments:
                print_helpful_hints("c04_architecture.md", "'Aha!' moments section")
            if not has_debugging:
                print_helpful_hints("c04_architecture.md", "Debugging scenarios")
            all_passed = False
    else:
        print_result("c04_architecture.md: File missing", False)
        print_helpful_hints("c04_architecture.md")
        all_passed = False

    print(f"\n{BLUE}--- Self-Learning Module Checks ---{RESET}\n")

    # Check explain.md (Flask example)
    explain_path = mission_dir / "explain.md"
    if _check_text_file(explain_path, 1500, keywords=[
        "flask", "@app.route",  # Flask-specific
        "line 4", "line 7",     # Line-specific questions
        "compare",              # Comparison questions
        "blog"                  # Transfer challenge
    ]):
        print_result("explain.md: Flask example with line-specific analysis ✓", True)
    else:
        print_result("explain.md: Missing, incomplete, or wrong format", False)
        print_helpful_hints("explain.md")
        all_passed = False

    # Check debug_detective.md
    debug_detective_path = mission_dir / "debug_detective.md"
    if _check_text_file(debug_detective_path, 1000, keywords=[
        "bug", "predict", "fix", "plugin", "module"
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
        
        has_architecture = "BaseNotification" in bad_code_text or "class Base" in bad_code_text
        
        if has_all_stages and has_architecture and len(bad_code_text) >= 2000:
            print_result("bad_code.py: All 4 stages with architecture pattern ✓", True)
        else:
            print_result("bad_code.py: Missing stages or architecture", False)
            print_helpful_hints("bad_code.py")
            all_passed = False
    else:
        print_result("bad_code.py: File missing", False)
        all_passed = False

    # Check bad_code_explain.md (5-part structure)
    bad_code_explain_path = mission_dir / "bad_code_explain.md"
    if _check_text_file(bad_code_explain_path, 2000, keywords=[
        "improvement ratio",    # Part 1: Metrics
        "teammate",            # Part 2: Team
        "rule of three",       # Part 4: When not to
        "inkypi",             # Part 5: Connection
        "real-world"           # Part 5: Examples
    ]):
        print_result("bad_code_explain.md: 5-part architecture analysis ✓", True)
    else:
        print_result("bad_code_explain.md: Missing, incomplete, or lacks depth", False)
        print_helpful_hints("bad_code_explain.md")
        all_passed = False

    # ==================================================
    # FINAL SUMMARY
    # ==================================================
    
    print(f"\n{BLUE}{'='*60}{RESET}")
    if all_passed:
        print_completion_feedback()
        
        print(f"{GREEN}📝 Your Deliverables:{RESET}")
        print(f"  • c04_architecture.md: System flow diagram + insights")
        print(f"  • explain.md: Flask architecture analysis")
        print(f"  • debug_detective.md: Bug tracing exercise")
        print(f"  • bad_code.py: Architecture refactoring (4 stages)")
        print(f"  • bad_code_explain.md: Metrics-driven analysis\n")
        
        print(f"{BLUE}💡 How to Use This Knowledge:{RESET}")
        print("  1. When debugging: Reference your architecture diagram")
        print("  2. When reading new code: Use the tracing techniques")
        print("  3. When designing: Think architecture patterns (Base + Implementations)")
        print("  4. In M-08: You'll know exactly where your image-loading code fits!\n")
    else:
        print(f"{RED}MISSION NOT COMPLETE{RESET}")
        print(f"\n{YELLOW}Review the hints above and complete missing items.{RESET}")
        print(f"{YELLOW}Then run 'python3 check.py' again.{RESET}\n")
        
        print(f"{BLUE}💡 Remember:{RESET}")
        print("  This is a READING mission, not a writing mission.")
        print("  Focus on understanding HOW the system works.")
        print("  Your deliverable is DOCUMENTATION (diagrams + analysis), not code.\n")


if __name__ == "__main__":
    check_mission()
