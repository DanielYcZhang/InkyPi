# Mission Instructions: The Inheritance Practice

**Objective**: Build a base card class and a specialized card that extends it.

---

## Outcome (Visible Result)
A card appears with a base layout plus a special badge added by the subclass.

---

## Glossary (Mission Terms)
- **Base class**: The shared foundation.
- **Subclass**: A specialized version of the base class.
- **Inheritance**: The “is-a” relationship.
- **super()**: Call the parent’s method.

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
mkdir -p src/plugins/c03_inheritance_practice
```

---

### Step 2: Register the Plugin (plugin-info.json)
Create this file:
Open `src/plugins/c03_inheritance_practice/plugin-info.json` in VS Code.

Put this inside:
```json
{
  "display_name": "C03 Inheritance Practice",
  "id": "c03_inheritance_practice",
  "class": "InheritancePractice"
}
```

---

### Step 3: Start from the Template
Copy the prefilled template:
```bash
cp academy/missions/c03_inheritance_practice/c03_inheritance_practice.py src/plugins/c03_inheritance_practice/c03_inheritance_practice.py
```

Then open it:
Open `src/plugins/c03_inheritance_practice/c03_inheritance_practice.py` in VS Code.

Follow the TODOs in the file.

---

## Teach (Concepts)
- **Base class**: shared drawing and layout.
- **Inheritance**: a specialized card that reuses the base.
- **super()**: call the parent’s setup or drawing.

---

## Use vs Avoid
- **Inheritance**: use when the subclass is a true “is-a.”
- **super()**: use to reuse parent logic instead of copying it.

---

## Concept Checkpoints
- Explain why `PetCard` is a subclass of `BaseCard`.
- Explain what `super()` does in the constructor.
- Explain what extra part the subclass adds.

---

## Practice (Tiny Exercises)
- Change the badge text and location.
- Add a second badge or icon.
- Change the base card title.

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
1) Start a new Copilot Chat titled `C-03 Explain-Back`.
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
- The base card appears.
- The subclass adds something extra.
- `super()` is called at least once.
- `bad_code.py` runs and prints drawing steps.

---

## Surprise (The Wow Moment)
Add a “rank badge” in the corner with a tiny icon or symbol.

---

## Stretch (Optional)
- Add a second subclass with a different badge style.
- Add a footer bar shared by all cards.

---

## Reflection
- What did `super()` save you from repeating?
- When would inheritance be a bad idea?

---

## Step 4: Add an Icon
Add:
- `src/plugins/c03_inheritance_practice/icon.png`

Fast option (temporary):
```bash
cp src/plugins/clock/icon.png src/plugins/c03_inheritance_practice/icon.png
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
cd ~/InkyPi/academy/missions/c03_inheritance_practice
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
