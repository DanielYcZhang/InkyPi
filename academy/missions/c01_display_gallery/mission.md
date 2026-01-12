# Mission Instructions: The Display Gallery

**Objective**: Build a plugin that draws three labeled boxes in a clean row.

---

## Outcome (Visible Result)
A simple “gallery wall” with three boxes and labels appears on the e-ink display.

---

## Glossary (Mission Terms)
- **Variable**: A labeled container for a value.
- **Coordinate**: A position like `(x, y)` on the screen.
- **Tuple**: A grouped value like `(x, y)` or `(r, g, b)`.
- **Label**: Text drawn on the image.
- **Padding**: Empty space around the edges.

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
mkdir -p src/plugins/c01_display_gallery
```

---

### Step 2: Register the Plugin (plugin-info.json)
Create this file:
Open `src/plugins/c01_display_gallery/plugin-info.json` in VS Code.

Put this inside:
```json
{
  "display_name": "C01 Display Gallery",
  "id": "c01_display_gallery",
  "class": "DisplayGallery"
}
```

---

### Step 3: Start from the Template
Copy the prefilled template:
```bash
cp academy/missions/c01_display_gallery/c01_display_gallery.py src/plugins/c01_display_gallery/c01_display_gallery.py
```

Then open it:
Open `src/plugins/c01_display_gallery/c01_display_gallery.py` in VS Code.

Follow the TODOs in the file.

---

## Teach (Concepts)
- **Variables**: name your layout numbers so you can tweak them easily.
- **Functions + parameters**: know what a function needs by reading its signature.
- **Coordinates**: place boxes using `(x, y)` positions.
- **Tuples**: use tuples for positions and colors.
- **Loops**: repeat a drawing step instead of copy-pasting.

---

## Use vs Avoid
- **Variables**: use for padding, spacing, and sizes; avoid magic numbers everywhere.
- **Function signatures**: use docs or `help()` to find required parameters; avoid guessing.
- **Coordinates**: use `(x, y)` pairs; avoid guessing positions without using `w` and `h`.
- **Tuples**: use for grouped values; avoid mixing the order.
- **Loops**: use for repeated shapes; avoid copy-pasting.

---

## Concept Checkpoints
- Explain why `padding` is a variable instead of a one-off number.
- Explain what `(x, y)` means on the screen.
- Explain what parameters `Image.new(...)` expects and why.
- Explain why we use `w` and `h` instead of hard-coding numbers.
- Explain why a loop is used to draw multiple boxes.

---

## Practice (Tiny Exercises)
- Increase the padding and see how the layout changes.
- Change the label text to something fun.
- Make one box wider than the others.

---

## Do-It Challenges (Hands-On)
- Use `help(Image.new)` in a Python shell and write a one-line comment in your code describing its parameters.
- Change the background to a light gray (e.g., `(230, 230, 230)`) and explain what each number means.
- Increase `box_count` to 4 and fix the labels so they still look neat.

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
1) Start a new Copilot Chat titled `C-01 Explain-Back`.
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
- Three labeled boxes are visible.
- Changing one variable (like padding) visibly changes the layout.
- `bad_code.py` runs and prints drawing steps.

---

## Surprise (The Wow Moment)
Add a tiny “gallery stamp” in the corner with two letters (your initials).

---

## Stretch (Optional)
- Center the three boxes on the screen.
- Add a small divider line between boxes.

---

## Reflection
- Which variable had the biggest impact on the layout?
- What would you change if the screen was twice as wide?

---

## Step 4: Add an Icon
Add:
- `src/plugins/c01_display_gallery/icon.png`

Fast option (temporary):
```bash
cp src/plugins/clock/icon.png src/plugins/c01_display_gallery/icon.png
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
cd ~/InkyPi/academy/missions/c01_display_gallery
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

---

## Mini-Lesson: Reading Function Signatures
When you call a function, it only works if you pass the right parameters in the right order.

Ways to find the required parameters:
- **Docs**: look up the function on the library site.
- **Python help()**: open a Python shell and run `help(Image.new)`.
- **Examples**: search the codebase for `Image.new(` and copy a working pattern.

Example:
```py
img = Image.new("RGB", (w, h), (255, 255, 255))
```
Signature idea: `Image.new(mode, size, color)` means you must pass:
- `mode`: the pixel format (like `"RGB"`).
- `size`: `(width, height)` as a tuple.
- `color`: background color `(r, g, b)`.
