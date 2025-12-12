# Mission Instructions: Protocol "Eyes Only"

**Objective**: Verify your secure connection, identify your network face, and create a "Top Secret" file that only YOU can read.

## Step 1: Reconnaissance
1.  Connect to your InkyPi via SSH.
2.  Run `ifconfig` (Interface Config).
    *   Find `wlan0`. This is your wireless badge.
    *   Note down your `inet` (IP Address). This is your identity on the network.

## Step 2: The Secret Documents
You are going to create a classified file that stores your "Commander Name".

1.  Navigate to the academy folder:
    ```bash
    cd ~/InkyPi/academy/missions/m01_commander
    ```
2.  Create a new file called `identity.txt`:
    ```bash
    nano identity.txt
    ```
3.  Inside, write your Commander Name (e.g., "Commander Fred").
4.  Save and Exit (Ctrl+O, Enter, Ctrl+X).

## Step 3: Lockdown (Permissions)
Right now, your file might be readable by others!
1.  Check the guards:
    ```bash
    ls -l identity.txt
    ```
    *Look at the `-rw-r--r--` part. The `r--` at the end means "Others can read it". This is unacceptable.*
2.  Secure the file:
    ```bash
    chmod 600 identity.txt
    ```
3.  Check again:
    ```bash
    ls -l identity.txt
    ```
    *It should now look like `-rw-------`. Total lockdown.*

## Step 4: Verification
Run the verification script to confirm your security protocols are active.
```bash
python3 check.py
```
