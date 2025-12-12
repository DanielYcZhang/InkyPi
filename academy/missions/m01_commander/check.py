import os
import sys
import stat

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
    print("Initiating Protocol Verification...\n")
    all_passed = True
    
    # 1. Check File Existence
    target_file = "identity.txt"
    if os.path.exists(target_file):
        print_result(f"Found classified file: {target_file}", True)
        
        # 2. Check Content
        with open(target_file, 'r') as f:
            content = f.read().strip()
        if len(content) > 0:
             print_result(f"Identity confirmed: {content}", True)
        else:
             print_result("File is empty! We need a Commander Name.", False)
             all_passed = False

        # 3. Check Permissions (The Core Challenge)
        st = os.stat(target_file)
        # Convert mode to octal (e.g., 0o600)
        mode = oct(st.st_mode)[-3:]
        
        if mode == "600":
            print_result("Security Access Level: 600 (Perfect Lockdown)", True)
        else:
            print_result(f"Security Alert! Current Permissions: {mode}. Required: 600", False)
            print("  -> Hint: Use 'chmod 600 identity.txt'")
            all_passed = False
            
    else:
        print_result(f"Missing file: {target_file}", False)
        print("  -> Did you create it inside the 'm01_commander' folder?")
        all_passed = False

    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. Welcome aboard, Commander.{RESET}")
        print("You have mastered the basics of System Ownership.")
    else:
        print(f"{RED}MISSION FAILED. Review security protocols.{RESET}")

if __name__ == "__main__":
    check_mission()
