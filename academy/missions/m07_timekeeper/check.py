import ast
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


def _parse_python(path: Path) -> ast.AST:
    with path.open("r", encoding="utf-8") as f:
        return ast.parse(f.read(), filename=str(path))


def _class_inherits_baseplugin(class_node: ast.ClassDef) -> bool:
    for base in class_node.bases:
        if isinstance(base, ast.Name) and base.id == "BasePlugin":
            return True
        if isinstance(base, ast.Attribute) and base.attr == "BasePlugin":
            return True
    return False


def _find_method(class_node: ast.ClassDef, method_name: str) -> Optional[ast.FunctionDef]:
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            return node
    return None


def _method_has_return(method_node: ast.FunctionDef) -> bool:
    for node in ast.walk(method_node):
        if isinstance(node, ast.Return) and node.value is not None:
            return True
    return False


def _imports_datetime(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "datetime":
            for alias in node.names:
                if alias.name == "datetime":
                    return True
    return False


def _uses_datetime_now(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "now":
                # datetime.now(...)
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "datetime":
                    return True
    return False


def _uses_strftime(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "strftime":
                return True
    return False


def _uses_fstring(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            return True
    return False


def check_mission():
    print("Initiating Timekeeper Verification...\n")
    all_passed = True

    repo_root = find_repo_root(Path.cwd())
    if not repo_root:
        print_result("Could not locate repo root (expected to find src/plugins).", False)
        print("  -> Hint: run this inside the InkyPi repo, e.g. ~/InkyPi/academy/missions/m07_timekeeper")
        return
    print_result(f"Repo root detected: {repo_root}", True)

    plugin_id = "m07_timekeeper"
    plugin_dir = repo_root / "src" / "plugins" / plugin_id

    if plugin_dir.is_dir():
        print_result(f"Plugin folder exists: src/plugins/{plugin_id}", True)
    else:
        print_result(f"Missing plugin folder: src/plugins/{plugin_id}", False)
        print("  -> Hint: mkdir -p src/plugins/m07_timekeeper")
        return

    plugin_info_path = plugin_dir / "plugin-info.json"
    if not plugin_info_path.is_file():
        print_result("Missing file: plugin-info.json", False)
        print("  -> Hint: create src/plugins/m07_timekeeper/plugin-info.json")
        return

    try:
        plugin_info = _read_json(plugin_info_path)
        print_result("plugin-info.json is valid JSON", True)
    except Exception as e:
        print_result(f"plugin-info.json is not valid JSON: {e}", False)
        return

    if plugin_info.get("id") == plugin_id:
        print_result(f"Plugin id matches folder name: {plugin_id}", True)
    else:
        print_result(f"Plugin id mismatch: expected '{plugin_id}', found '{plugin_info.get('id')}'", False)
        all_passed = False

    class_name = plugin_info.get("class")
    if isinstance(class_name, str) and class_name.strip():
        print_result(f"Plugin class configured: {class_name}", True)
    else:
        print_result("Plugin class is missing or empty in plugin-info.json", False)
        all_passed = False
        class_name = None

    python_file = plugin_dir / f"{plugin_id}.py"
    if python_file.is_file():
        print_result(f"Python file exists: {python_file.name}", True)
    else:
        print_result(f"Missing python file: {python_file.name}", False)
        print(f"  -> Hint: create {python_file}")
        all_passed = False

    if python_file.is_file() and class_name:
        try:
            tree = _parse_python(python_file)
            print_result("Python file parses (no syntax errors)", True)
        except SyntaxError as e:
            print_result(f"Python syntax error: {e.msg} (line {e.lineno})", False)
            all_passed = False
            tree = None
        except Exception as e:
            print_result(f"Could not parse Python file: {e}", False)
            all_passed = False
            tree = None

        if tree:
            class_nodes = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == class_name]
            if not class_nodes:
                print_result(f"Class not found: {class_name}", False)
                all_passed = False
            else:
                class_node = class_nodes[0]
                if _class_inherits_baseplugin(class_node):
                    print_result(f"{class_name} inherits from BasePlugin", True)
                else:
                    print_result(f"{class_name} does not inherit from BasePlugin", False)
                    all_passed = False

                method = _find_method(class_node, "generate_image")
                if not method:
                    print_result("Missing method: generate_image(self, settings, device_config)", False)
                    all_passed = False
                else:
                    if _method_has_return(method):
                        print_result("generate_image returns a value", True)
                    else:
                        print_result("generate_image does not return a value", False)
                        all_passed = False

            if _imports_datetime(tree):
                print_result("Imports datetime via `from datetime import datetime`", True)
            else:
                print_result("Missing `from datetime import datetime` import", False)
                all_passed = False

            if _uses_datetime_now(tree):
                print_result("Uses datetime.now()", True)
            else:
                print_result("Did not detect datetime.now()", False)
                print("  -> Hint: now = datetime.now()")
                all_passed = False

            if _uses_strftime(tree):
                print_result("Uses strftime() for formatting", True)
            else:
                print_result("Did not detect strftime()", False)
                print("  -> Hint: time_text = now.strftime('%H:%M')")
                all_passed = False

            if _uses_fstring(tree):
                print_result("Uses an f-string", True)
            else:
                print_result("Did not detect an f-string", False)
                print("  -> Hint: label = f\"Time: {time_text}\"")
                all_passed = False

    icon_path = plugin_dir / "icon.png"
    if icon_path.is_file():
        print_result("Icon exists: icon.png", True)
    else:
        print_result("Missing icon.png", False)
        print("  -> Hint: copy one: cp src/plugins/clock/icon.png src/plugins/m07_timekeeper/icon.png")
        all_passed = False

    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. The Clock Obeys You.{RESET}")
    else:
        print(f"{RED}MISSION FAILED. Time is still broken.{RESET}")


if __name__ == "__main__":
    check_mission()

