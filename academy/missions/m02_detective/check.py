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
    print("Initiating Forensic Analysis...\n")
    
    target_file = "evidence.txt"
    expected_clue = "sector 7g" # Case insensitive check

    if not os.path.exists(target_file):
        print_result(f"Evidence file missing: {target_file}", False)
        print("  -> Did you save the sector name into 'evidence.txt'?")
        return

    with open(target_file, 'r') as f:
        content = f.read().strip().lower()

    if expected_clue in content:
        print_result(f"Evidence Verified: '{content}' matches intelligence reports.", True)
        print("\n-----------------------------")
        print(f"{GREEN}MISSION COMPLETE. Detective Rank Achieved.{RESET}")
        print("You can now find any error, anywhere, anytime.")
    else:
        print_result(f"Evidence Mismatch. Found: '{content}'", False)
        print(f"  -> The intelligence report said the package was in '{expected_clue}'.")
        print("  -> Use 'journalctl | grep secret_agent' to check again.")

if __name__ == "__main__":
    check_mission()
