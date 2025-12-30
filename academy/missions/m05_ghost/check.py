import subprocess
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

def run_command(cmd):
    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        return result.stdout.strip(), result.returncode
    except Exception as e:
        return "", -1

def check_mission():
    print("Initiating Ectoplasm Detection...\n")
    all_passed = True
    
    # 1. Check if Service File exists in system
    if os.path.exists("/etc/systemd/system/haunted.service"):
         print_result("Service File found in /etc/systemd/system", True)
    else:
         print_result("Service File NOT found in /etc/systemd/system details.", False)
         print("  -> Did you run 'sudo cp haunted.service ...'?")
         all_passed = False

    # 2. Check Service Status
    output, code = run_command("systemctl is-active haunted.service")
    
    if output == "active":
        print_result("Service Status: ACTIVE (The Ghost is alive!)", True)
    else:
        print_result(f"Service Status: {output} (The Ghost is unresponsive)", False)
        print("  -> Try 'sudo systemctl start haunted.service'")
        all_passed = False

    # 3. Check Enabled Status
    output, code = run_command("systemctl is-enabled haunted.service")
    if output == "enabled":
        print_result("Boot Startup: ENABLED (IMMORTAL)", True)
    else:
        print_result(f"Boot Startup: {output} (Mortal)", False)
        print("  -> Try 'sudo systemctl enable haunted.service'")
        all_passed = False

    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. You have created Life.{RESET}")
        print("Phase 1: System Engineer is COMPLETE.")
        print("You are now ready to start coding pixels.")
    else:
        print(f"{RED}MISSION FAILED. The ritual is incomplete.{RESET}")

if __name__ == "__main__":
    check_mission()
