# Mission Instructions: The Creature Card

**Objective**: Build a plugin that shows a creature card using a class and object.

---

## Outcome (Visible Result)
A creature card appears with a name, species, and level on the display.

---

## Glossary (Mission Terms)
- **Class**: A blueprint for making objects.
- **Object**: A specific thing built from a class.
- **Property**: A value stored on an object (like `self.name`).
- **Method**: A function inside a class.

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
mkdir -p src/plugins/c02_creature_card
```

---

### Step 2: Register the Plugin (plugin-info.json)
Create this file:
Open `src/plugins/c02_creature_card/plugin-info.json` in VS Code.

Put this inside:
```json
{
  "display_name": "C02 Creature Card",
  "id": "c02_creature_card",
  "class": "CreatureCard"
}
```

---

### Step 3: Start from the Template
Copy the prefilled template:
```bash
cp academy/missions/c02_creature_card/c02_creature_card.py src/plugins/c02_creature_card/c02_creature_card.py
```

Then open it:
Open `src/plugins/c02_creature_card/c02_creature_card.py` in VS Code.

Follow the TODOs in the file.

---

## Teach (Concepts)
- **Class vs Object**: the blueprint vs the real thing.
- **Properties**: store creature facts in `self`.
- **Methods**: draw the card using the creature’s data.

---

## Use vs Avoid
- **Classes**: use when you need a reusable “thing.”
- **Objects**: use to bundle related values together.
- **Properties**: use `self.*` to store data on the object.

---

## Concept Checkpoints
- Explain the difference between a class and an object.
- Explain why `self.name` is a property.
- Explain why `draw` belongs inside the class.

---

## Practice (Tiny Exercises)
- Change the creature’s name and species.
- Add a new property (like `favorite_food`) and draw it.
- Change where the text appears by adjusting coordinates.

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
1) Start a new Copilot Chat titled `C-02 Explain-Back`.
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
- A creature card displays at least three lines of text.
- The class has properties stored in `self`.
- The plugin uses the creature object to draw.
- `bad_code.py` runs and prints drawing steps.

---

## Surprise (The Wow Moment)
Add a tiny badge next to the name: a small box with the creature’s level.

---

## Stretch (Optional)
- Add a second creature card below the first.
- Add a border or divider line.

---

## Reflection
- What makes a property different from a normal variable?
- If you had 10 creatures, how would classes help?

---

## Step 4: Add an Icon
Add:
- `src/plugins/c02_creature_card/icon.png`

Fast option (temporary):
```bash
cp src/plugins/clock/icon.png src/plugins/c02_creature_card/icon.png
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
cd ~/InkyPi/academy/missions/c02_creature_card
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
