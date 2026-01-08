# Mission Instructions: The Artist

**Objective**: Create a plugin that draws your gamer tag (your name) plus simple shapes using Pillow’s drawing tools.

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
mkdir -p src/plugins/m08_artist
```

---

## Step 2: Register the Plugin (plugin-info.json)
Create this file:
```bash
nano src/plugins/m08_artist/plugin-info.json
```

Put this inside:
```json
{
  "display_name": "M08 Artist",
  "id": "m08_artist",
  "class": "Artist"
}
```

---

## Step 3: Write the Plugin Code (Python)
Create this file:
```bash
nano src/plugins/m08_artist/m08_artist.py
```

Your plugin must:
- Inherit from `BasePlugin`
- Implement `generate_image(self, settings, device_config)`
- Use `w, h = device_config.get_resolution()` (or equivalent)
- Create a Pillow image and a Draw object
- Draw text (your name) somewhere
- Draw at least **two** shapes (rectangle/line/ellipse)
- Use at least one tuple for a coordinate or color
- Use at least one `for` loop to draw a repeated pattern (3 dots, stripes, etc.)

Hint ideas:
- Draw a border rectangle around the canvas.
- Draw 3 dots evenly spaced along the bottom using a loop.
- Draw a diagonal line or a small “badge” box behind the name.

---

## Step 4: Add an Icon
Add:
- `src/plugins/m08_artist/icon.png`

Fast option (temporary):
```bash
cp src/plugins/clock/icon.png src/plugins/m08_artist/icon.png
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
cd ~/InkyPi/academy/missions/m08_artist
```

Run:
```bash
python3 check.py
```

