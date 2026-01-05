# Mission Instructions: The Awakening

**Objective**: Create your first real InkyPi plugin that renders a “Hello, \<Name\>” card.

This is the moment Python becomes **visible**.

---

## Step 0: Read the Briefing
Open and read:
- `briefing.md`

Pay attention to the “Syntax Cards” sections — they answer questions like what parentheses mean, what parameters are, and what `self` does.

---

## Step 1: Create Your Plugin Folder
From the InkyPi project root:
```bash
cd ~/InkyPi
```

Create the plugin directory:
```bash
mkdir -p src/plugins/m06_awakening
```

---

## Step 2: Register the Plugin (plugin-info.json)
Create this file:
```bash
nano src/plugins/m06_awakening/plugin-info.json
```

Put this inside (exact spelling matters):
```json
{
  "display_name": "M06 Awakening",
  "id": "m06_awakening",
  "class": "Awakening"
}
```

---

## Step 3: Write the Plugin Code (Python)
Create this file:
```bash
nano src/plugins/m06_awakening/m06_awakening.py
```

Write a plugin class that:
- Inherits from `BasePlugin`
- Implements `generate_image(self, settings, device_config)`
- Creates an image using Pillow
- Draws “Hello, \<Name\>” centered on the screen
- Returns the `Image` object

Hints:
- Use `device_config.get_resolution()` to get `(width, height)`
- Start with a solid background
- Use `settings.get("name", "Commander")` for the name

---

## Step 4: Add an Icon
Your plugin needs an icon file:
- `src/plugins/m06_awakening/icon.png`

Fast option (temporary): copy any existing icon:
```bash
cp src/plugins/clock/icon.png src/plugins/m06_awakening/icon.png
```

---

## Step 5: Restart InkyPi and See It in the Web UI
Restart the service:
```bash
sudo systemctl restart inkypi.service
```

Now open the InkyPi web UI, find your new plugin, and try generating the image.

---

## Step 6: Verification
Go back to this mission folder:
```bash
cd ~/InkyPi/academy/missions/m06_awakening
```

Run:
```bash
python3 check.py
```

If anything fails, read the hint, fix, and run it again.
