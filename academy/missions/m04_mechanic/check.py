import os
import signal

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
    print("Initiating Damage Report...\n")
    all_passed = True
    
    # --- CHECK 1: THE KILL ---
    report_file = "kill_report.txt"
    target_pid = None

    if os.path.exists(report_file):
        with open(report_file, 'r') as f:
            content = f.read().strip()
            if content.isdigit():
                target_pid = int(content)
                # Check if process is dead
                try:
                    os.kill(target_pid, 0)
                    print_result(f"Target PID {target_pid} is STILL ACTIVE!", False)
                    all_passed = False
                except OSError:
                    print_result(f"Confirmed: Target PID {target_pid} neutralized.", True)
            else:
                 print_result(f"Invalid Report. '{content}' is not a PID.", False)
                 all_passed = False
    else:
        print_result(f"Missing Kill Report: {report_file}", False)
        all_passed = False

    # --- CHECK 2: THE FIX ---
    code_file = "leaky_bucket.py"
    if os.path.exists(code_file):
        with open(code_file, 'r') as f:
            code = f.read()
        
        # Check if the leaking line is handled
        if "history.append(data)" in code:
            # Check if it's commented out
            if "# history.append(data)" in code or "#history.append(data)" in code:
                 print_result("Code Fix Verified: Memory Leak patched.", True)
            else:
                 # Check if the surrounding context implies it's still active
                 # Simple check: count occurrences vs commented occurrences
                 print_result("Memory Leak Detected! You didn't comment out the leaking line.", False)
                 all_passed = False
        else:
             print_result("Code Fix Verified: Leaking line deleted.", True)
    else:
        print_result(f"Missing File: {code_file}", False)
        all_passed = False


    print("\n-----------------------------")
    if all_passed:
        print(f"{GREEN}MISSION COMPLETE. Master Mechanic Status Confirmed.{RESET}")
    else:
        print(f"{RED}MISSION FAILED. Review objectives.{RESET}")

if __name__ == "__main__":
    check_mission()
