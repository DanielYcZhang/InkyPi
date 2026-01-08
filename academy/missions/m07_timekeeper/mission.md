# Mission Instructions: The Timekeeper

**Objective**: Create a plugin that displays the current time (and optionally date) using `datetime`, variables, and formatting.

---

## Step 0: Read the Briefing
Open and read:
- `briefing.md`

---

## Step 1: Create Your Plugin Folder
From the InkyPi project root:
```bash
cd ~/InkyPi
```

Create the plugin directory:
```bash
mkdir -p src/plugins/m07_timekeeper
```

---

## Step 2: Register the Plugin (plugin-info.json)
Create this file:
```bash
nano src/plugins/m07_timekeeper/plugin-info.json
```

Put this inside:
```json
{
  "display_name": "M07 Timekeeper",
  "id": "m07_timekeeper",
  "class": "Timekeeper"
}
```

---

## Step 3: Write the Plugin Code (Python)
Create this file:
```bash
nano src/plugins/m07_timekeeper/m07_timekeeper.py
```

Your plugin must:
- Inherit from `BasePlugin`
- Implement `generate_image(self, settings, device_config)`
- Import `datetime` using `from datetime import datetime`
- Create a variable like `now = datetime.now()`
- Format time into a string (use `strftime`)
- Use an f-string at least once (example: `f"Time: {time_text}"`)
- Draw the time text onto an image and return it

Hints:
- Use `device_config.get_resolution()` to get `(width, height)`
- Use a large font if you know how; otherwise just draw basic text first and improve later

---

## Step 4: Add an Icon
Add:
- `src/plugins/m07_timekeeper/icon.png`

Fast option (temporary):
```bash
cp src/plugins/clock/icon.png src/plugins/m07_timekeeper/icon.png
```

---

## Step 5: Restart InkyPi and Test in the Web UI
Restart the service:
```bash
sudo systemctl restart inkypi.service
```

Open the web UI, select your plugin, and generate the image.

---

## Step 6: Verification
Go back to this mission folder:
```bash
cd ~/InkyPi/academy/missions/m07_timekeeper
```

Run:
```bash
python3 check.py
```

