# Mission Instructions: Operation "Poltergeist"

**Objective**: Turn a python script into an immortal background service that survives a reboot.

## Step 1: The Mortal Script
1.  Run the script manually to confirm it works:
    ```bash
    python3 haunted_house.py
    ```
    *It prints "BOO!" every 10 seconds.*
2.  Stop it with `Ctrl+C`.
    *See? It died. We need to make it immortal.*

## Step 2: The Recipe
We have provided a template file `haunted.service`. You need to customize it.
1.  Find your current folder path:
    ```bash
    pwd
    ```
    *Copy this path (e.g., `/home/pi/InkyPi/academy/missions/m05_ghost`).*
2.  Edit the service file:
    ```bash
    nano haunted.service
    ```
3.  Find `[YOUR_PATH]` and replace it with the path you copied.
    *Result format: `ExecStart=/usr/bin/python3 /home/pi/.../haunted_house.py`*
4.  Save and Exit.

## Step 3: The Summoning
Systemd lives in `/etc/systemd/system`. We need to copy our recipe there.
1.  Copy the file (Needs Root power):
    ```bash
    sudo cp haunted.service /etc/systemd/system/
    ```
2.  Tell systemd to read the new file:
    ```bash
    sudo systemctl daemon-reload
    ```

## Step 4: The Invocation
Now we turn it on.
1.  Start the ghost:
    ```bash
    sudo systemctl start haunted.service
    ```
2.  Enable it (So it starts on boot):
    ```bash
    sudo systemctl enable haunted.service
    ```
3.  Check if it's alive:
    ```bash
    systemctl status haunted.service
    ```
    *You should see a green dot and `Active: active (running)`.*

## Step 5: The Listeners
Verify it is actually haunting the logs.
1.  Use the skills you learned in **Mission 02 (The Detective)**:
    ```bash
    journalctl -u haunted -f
    ```
    *You should see "Scary Ghost Noise: BOO!" appearing every 10 seconds.*

## Step 6: Verification
Run the verification script.
```bash
python3 check.py
```
