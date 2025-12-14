# Mission Instructions: Operation "Raw Metal"

**Objective**: Prove you can command the machine's physical state without writing a single line of Python.

## Step 1: The Sensor (Reading)
The CPU is hot. How hot?
1.  Navigate to the thermal zone:
    ```bash
    cd /sys/class/thermal/thermal_zone0
    ```
2.  Read the temperature file:
    ```bash
    cat temp
    ```
    *You will see a large number like `45123`. This is millidegrees Celsius. (45.123°C).*
3.  **Record your finding**:
    *   Create a file `cpu_temp.txt` in your mission folder (`~/InkyPi/academy/missions/m03_alchemist`).
    *   Write the number you found into it.

## Step 2: The Heartbeat (Writing)
Now, let's touch the Green Activity LED (ACT).
1.  Navigate to the LED controller:
    *   On Pi Zero 2 W, it is usually here:
        ```bash
        cd /sys/class/leds/ACT
        ```
        *(If not found, try `cd /sys/class/leds/led0`)*
2.  Check the current state (0 or 255):
    ```bash
    cat brightness
    ```
3.  **The Transmutation**: Turn it OFF.
    *   Normally we use `echo 0 > brightness`, but standard user cannot touch hardware. We need a "Root Shell" trick:
    ```bash
    echo 0 | sudo tee brightness
    ```
    *Look at your Pi. The Green LED should be DEAD.*
4.  Turn it back ON:
    ```bash
    echo 1 | sudo tee brightness
    ```
    *It lives!*

## Step 3: The Evidence
We need to prove you found the correct LED path.
1.  In your mission folder (`~/InkyPi/academy/missions/m03_alchemist`).
2.  Create a file named `led_path.txt`.
3.  Write the full path to the LED you managed to control (e.g., `/sys/class/leds/ACT`).

## Step 4: Verification
Run the verification script to confirm your mastery of the elements.
```bash
python3 check.py
```
