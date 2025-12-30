import time
import sys

# THE HAUNTED HOUSE
# This script is a "Daemon". It runs forever in the background.

print("The House is Awake...")

def main():
    while True:
        # We print to "Standard Output"
        # When running as a service, systemd catches this and puts it in the Journal (Logs)
        print("Scary Ghost Noise: BOO!", flush=True)
        
        # Adding flush=True is important! 
        # Daemons sometimes hold their breath (buffer output) unless you tell them to flush.
        
        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("The Ghost has been banished.")
