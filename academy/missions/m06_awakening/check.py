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


def check_mission():
    print("Initiating Plugin Awakening Scan...\n")
    all_passed = True

    repo_root = find_repo_root(Path.cwd())
    if not repo_root:
        print_result("Could not locate repo root (expected to find src/plugins).", False)
        print("  -> Hint: run this inside the InkyPi repo, e.g. ~/InkyPi/academy/missions/m06_awakening")
        return
    print_result(f"Repo root detected: {repo_root}", True)

    plugin_id = "m06_awakening"
    plugin_dir = repo_root / "src" / "plugins" / plugin_id

    if plugin_dir.is_dir():
        print_result(f"Plugin folder exists: src/plugins/{plugin_id}", True)
    else:
        print_result(f"Missing plugin folder: src/plugins/{plugin_id}", False)
        print("  -> Hint: mkdir -p src/plugins/m06_awakening")
        return

    plugin_info_path = plugin_dir / "plugin-info.json"
    if not plugin_info_path.is_file():
        print_result("Missing file: plugin-info.json", False)
        print("  -> Hint: create src/plugins/m06_awakening/plugin-info.json")
        return

    try:
        plugin_info = _read_json(plugin_info_path)
        print_result("plugin-info.json is valid JSON", True)
    except Exception as e:
        print_result(f"plugin-info.json is not valid JSON: {e}", False)
        return

    expected_keys = ["display_name", "id", "class"]
    missing = [k for k in expected_keys if k not in plugin_info]
    if missing:
        print_result(f"plugin-info.json missing keys: {', '.join(missing)}", False)
        all_passed = False

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
                print(f"  -> Hint: define `class {class_name}(BasePlugin):` in {python_file.name}")
                all_passed = False
            else:
                class_node = class_nodes[0]
                if _class_inherits_baseplugin(class_node):
                    print_result(f"{class_name} inherits from BasePlugin", True)
                else:
                    print_result(f"{class_name} does not inherit from BasePlugin", False)
                    print(f"  -> Hint: `class {class_name}(BasePlugin):`")
                    all_passed = False

                method = _find_method(class_node, "generate_image")
                if not method:
                    print_result("Missing method: generate_image(self, settings, device_config)", False)
                    all_passed = False
                else:
                    arg_names = [a.arg for a in method.args.args]
                    if len(arg_names) >= 3 and arg_names[0] == "self":
                        print_result(f"generate_image args look OK: {', '.join(arg_names[:3])}", True)
                    else:
                        print_result(f"generate_image args look unusual: {', '.join(arg_names)}", False)
                        print("  -> Hint: def generate_image(self, settings, device_config):")
                        all_passed = False

                    if _method_has_return(method):
                        print_result("generate_image returns a value", True)
                    else:
                        print_result("generate_image does not return a value", False)
                        print("  -> Hint: create an image and `return img`")
                        all_passed = False

    icon_path = plugin_dir / "icon.png"
    if icon_path.is_file():
        print_result("Icon exists: icon.png", True)
    else:
        print_result("Missing icon.png", False)
        print("  -> Hint: copy one: cp src/plugins/clock/icon.png src/plugins/m06_awakening/icon.png")
        all_passed = False

    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. The Plugin has Awakened.{RESET}")
        print("Next: make it configurable with settings (M-07+).")
    else:
        print(f"{RED}MISSION FAILED. The Plugin is still sleeping.{RESET}")


if __name__ == "__main__":
    check_mission()
