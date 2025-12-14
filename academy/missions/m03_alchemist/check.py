import os

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_result(msg, success):
    if success:
        print(f"[{GREEN}PASS{RESET}] {msg}")
    else:
        print(f"[{RED}FAIL{RESET}] {msg}")

def check_mission():
    print("Initiating Elemental Analysis...\n")
    all_passed = True
    
    # 1. Check CPU Temperature
    temp_file = "cpu_temp.txt"
    if os.path.exists(temp_file):
        with open(temp_file, 'r') as f:
            content = f.read().strip()
        
        if content.isdigit() and 10000 < int(content) < 100000:
             print_result(f"CPU Temperature Reading Valid: {content} mC", True)
        else:
             print_result(f"Invalid Temperature: {content}. Expected a number like 45000.", False)
             all_passed = False
    else:
        print_result(f"Missing file: {temp_file}", False)
        all_passed = False

    # 2. Check LED Path
    led_file = "led_path.txt"
    if os.path.exists(led_file):
        with open(led_file, 'r') as f:
            path = f.read().strip()
            
        if os.path.exists(path) and "leds" in path:
             print_result(f"LED Path Confirmed: {path}", True)
        else:
             print_result(f"Invalid LED Path: {path}. System cannot find this device.", False)
             all_passed = False
    else:
        print_result(f"Missing file: {led_file}", False)
        all_passed = False

    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. You are now an Alchemist.{RESET}")
        print("Remember: There is no magic. Only Files.")
    else:
        print(f"{RED}MISSION FAILED. The elements did not respond.{RESET}")

if __name__ == "__main__":
    check_mission()
