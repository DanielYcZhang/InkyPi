# Mission Instructions: Operation "Needle in a Haystack"

**Objective**: A secret agent has left a coded message in the system logs. Your mission is to filter through the noise and retrieve it.

## Step 1: Plant the Evidence
First, we need to create a log entry. Linux has a tool called `logger` that writes directly to the system journal.
1.  Run the following command to plant a simulated secret:
    ```bash
    logger -t secret_agent "The package is hidden in sector 7G"
    ```
    *Nothing happened? Correct. It wrote silently to the background diary.*

## Step 2: The Overwhelming Noise
1.  Try to find your message by reading the whole journal:
    ```bash
    journalctl
    ```
2.  **STOP!** It's too much text. Press `q` to quit. You will never find it this way.

## Step 3: The Filter
Now, use your detective skills.
1.  Use `grep` to search for the "tag" we used (`secret_agent`):
    ```bash
    journalctl | grep "secret_agent"
    ```
2.  You should see a line pop up with a timestamp and your message.
    *Example: Dec 12 10:00:00 raspberrypi secret_agent: The package is hidden in sector 7G*

## Step 4: Record the Findings
1.  Create a file named `evidence.txt` inside the `m02_detective` folder.
2.  Write **only the sector name** that was mentioned in the secret message (e.g., `sector 7G`).
3.  Save the file.

## Step 5: Verification
Run the verification script to confirm you caught the right suspect.
```bash
python3 check.py
```
