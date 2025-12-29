import time
import os
import sys

# Colors for dramatic effect
RED = "\033[91m"
RESET = "\033[0m"

def rogue_drone():
    pid = os.getpid()
    print(f"\n{RED}!!! WARNING: ROGUE DRONE ACTIVATED !!!{RESET}")
    print(f"Drone PID: {pid}")
    print("I am consuming system resources...")
    print("Try to stop me before I reach 100% capacity!\n")

    usage = []
    bloat_factor = "X" * 1024 * 1024 # 1MB of text chunk

    try:
        for i in range(1, 101):
            # Consume Memory
            usage.append(bloat_factor)
            
            # Print status
            print(f"[DRONE {pid}] Consuming RAM... Capacity: {i}%")
            
            # Write to a file so we can check if it's still alive later
            with open("drone_status.txt", "w") as f:
                f.write(f"ALIVE\n{pid}")

            time.sleep(2) # Give the student time to react
            
        print(f"\n{RED}[CRITICAL] MAX CAPACITY REACHED. SYSTEM COMPROMISED.{RESET}")

    except KeyboardInterrupt:
        print("\nNice try using Ctrl+C... but in a real server, you might not be in this window!")

if __name__ == "__main__":
    rogue_drone()
