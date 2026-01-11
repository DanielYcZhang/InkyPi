# Mission Instructions: The Artist

**Objective**: Create a plugin that draws your gamer tag (your name) plus simple shapes using Pillow’s drawing tools.

---

## Outcome (Visible Result)
A custom “tag art” image appears on the e-ink display: your name plus a simple shape pattern (dots/stripes/badge).

---

## Glossary (Mission Terms)
- **Pillow**: A Python library for creating and drawing on images.
- **Image**: A canvas you can draw on.
- **Draw**: A helper object that draws shapes and text onto an image.
- **Coordinate**: A position like `(x, y)` on the screen.
- **Tuple**: A small grouped value like `(x, y)` or `(r, g, b)`.
- **Loop**: A way to repeat an action, like drawing 3 dots in a row.
- **Method**: A function that belongs to a class.

---

## Step 0: Read the Briefing
Open and read:
- `briefing.md`

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

## Teach (Concepts)
- **Pillow**: creates images and gives you drawing tools.
- **Coordinates**: `(0, 0)` is the top-left. X goes right, Y goes down.
- **Tuples**: use `(x, y)` for positions and `(r, g, b)` for colors.
- **Loops**: use a `for` loop to repeat simple drawing steps.

---

## Use vs Avoid
- **Coordinates**: use `(x, y)` pairs; avoid “magic numbers” with no labels.
- **Tuples**: use for grouped data (position or color); avoid mixing up order.
- **Loops**: use for repeated shapes; avoid copy-pasting the same line 3 times.

---

## Concept Checkpoints
- Explain what `(0, 0)` means on the screen.
- Explain why we use a loop to draw repeated dots.
- Explain what a tuple is in this mission.

---

## Practice (Tiny Exercises)
- Move your name by changing the text `(x, y)` coordinates.
- Change the border thickness or add a second border.
- Make your dot pattern wider by increasing spacing.

---

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
Add a small “stamp” in a corner: a tiny box with two letters (like `XP` or your initials).

---

## Stretch (Optional)
- Compute positions based on `w` and `h` so the layout scales.
- Add a second line of text (nickname or rank).

---

## Reflection
- What was the hardest part about placing shapes?
- What did the loop save you from doing by hand?

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

---

## Workflow (VS Code + GitHub + Raspberry Pi)
Use VS Code instead of Nano. Keep this flow:

1. On your MacBook, edit in VS Code and commit your changes.
2. Push the branch to GitHub.
3. SSH into the Raspberry Pi.
4. In the Pi repo, run `git fetch`, then check out your branch.
5. Restart the service and test.
