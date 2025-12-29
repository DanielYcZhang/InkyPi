# Mission Instructions: Operation "Emergency Stop"

**Objective**: Master the art of Resource Management by killing rogue processes and fixing memory leaks.

## Part 1: The Killer (Signals)
1.  **Launch the Threat**:
    Open a terminal and run `rogue_drone.py`.
    ```bash
    python3 rogue_drone.py
    ```
    *It will start eating memory.*

2.  **Identify the Target**:
    Open a second terminal. Find the PID:
    ```bash
    ps aux | grep drone
    ```
    *Find the PID number (e.g., 1234).*

3.  **Terminate**:
    Kill it before it crashes the system.
    ```bash
    kill -9 [PID]
    ```

4.  **Report**:
    Create `kill_report.txt` and write the PID you killed inside it.

---

## Part 2: The Surgeon (Debugging)
You stopped the bleeding, but now you must fix the wound.
We found another script `leaky_bucket.py` that keeps crashing the servers.

1.  **Analyze the Code**:
    Open `leaky_bucket.py` in your editor.
    ```bash
    nano leaky_bucket.py
    ```
    *Read the comments. Look for the "BUG ZONE".*

2.  **Understand the Leak**:
    The program creates a `data` variable (1MB size).
    It then `appends` it to the global `history` list.
    Since the loop runs forever, the list grows forever until RAM is full.

3.  **Fix the Bug**:
    We don't need to save the history!
    **Comment out** or **Delete** the line that causes the leak:
    ```python
    # history.append(data)
    ```

4.  **Test the Fix**:
    Run the script again.
    ```bash
    python3 leaky_bucket.py
    ```
    *It should now run forever without the "History size" increasing excessively.*

## Part 3: Verification
Run the check script.
```bash
python3 check.py
```
