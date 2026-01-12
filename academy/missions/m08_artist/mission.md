# Mission Instructions: The Artist

**Objective**: Create a plugin that draws your gamer tag (your name) plus simple shapes using Pillow’s drawing tools.

---

## Outcome (Visible Result)
A custom “tag art” image appears on the e-ink display: your name plus a simple shape pattern (dots/stripes/badge).

---

## Concepts You Will Learn (List Only)
- Pillow Image + Draw
- Coordinates
- Tuples
- Loops

---

## Glossary (with Examples)
- **Pillow**: Python image library. Example: `Image.new(...)`.
- **Image**: A canvas you draw on. Example: `img = Image.new(...)`.
- **Draw**: A helper that draws shapes/text. Example: `draw = ImageDraw.Draw(img)`.
- **Coordinate**: A position like `(x, y)`. Example: `text_pos = (20, 20)`.
- **Tuple**: A grouped value like `(x, y)` or `(r, g, b)`.
- **Loop**: Repeat actions. Example: `for i in range(3):`.

---

## Step 0: Read the Briefing
Open and read:
- `briefing.md`

This is where the concept explanations and analogies live.

---

## Build (Steps)

### Step 1: Create Your Plugin Folder
From the InkyPi project root:
```bash
cd ~/InkyPi
```

Create the plugin directory:
```bash
mkdir -p src/plugins/m08_artist
```

---

### Step 2: Register the Plugin (plugin-info.json)
Create this file:
Open `src/plugins/m08_artist/plugin-info.json` in VS Code.

Put this inside:
```json
{
  "display_name": "M08 Artist",
  "id": "m08_artist",
  "class": "Artist"
}
```

---

### Step 3: Write the Plugin Code (Python)
Start from the prefilled template in this mission folder:
```bash
cp academy/missions/m08_artist/m08_artist.py src/plugins/m08_artist/m08_artist.py
```

Then open `src/plugins/m08_artist/m08_artist.py` in VS Code to edit.

Follow the TODOs in the template for practice tasks and the surprise.

## Self-Learning Module (Required)
Fill these files in this mission folder:
- `explain.md`
- `predict.md`
- `trace.md`
- `bad_code.py`
- `bad_code_explain.md`

Then run:
```bash
python3 check.py
```
This generates `copilot_input.txt` for you.

**Copilot workflow**
1) Start a new Copilot Chat titled `M-08 Explain-Back`.
2) Open `copilot_input.txt`, copy all, and paste into Copilot Chat.
3) If Copilot says you missed something, keep chatting until you fix it.
4) Update `explain.md` and re-run `python3 check.py`.

**Bad code practice**
- Open `bad_code.py`, fix it, then run:
```bash
python3 bad_code.py
```
- You should see text output that describes what would be drawn.

---

## Check (Acceptance Criteria)
- The plugin appears in the web UI.
- The display shows your name and at least two shapes.
- There is a repeated pattern drawn by a loop.
- `bad_code.py` runs and prints drawing steps.

---

## Surprise (The Wow Moment)
Complete the **Surprise** TODO inside `m08_artist.py`.

---

## Stretch (Optional)
Complete any **Stretch** TODOs inside `m08_artist.py`.

---

## Reflection
Answer the Reflection prompt inside `explain.md`.

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

---

## Workflow (VS Code + GitHub + Raspberry Pi)
Use VS Code instead of Nano. Keep this flow:

1. On your MacBook, edit in VS Code and commit your changes.
2. Push the branch to GitHub.
3. SSH into the Raspberry Pi.
4. In the Pi repo, run `git fetch`, then check out your branch.
5. Restart the service and test.
