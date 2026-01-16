# InkyPi Academy Syllabus

## 1. The Strategy: "The Plugin Factory"
Instead of writing throwaway scripts, the student will build **Real InkyPi Plugins** for every mission.
- **The Context:** "You are an Engineer extending the capabilities of this device."
- **The Result:** Every mission ends with a permanent, usable feature on their wall.
- **The Delivery:**
    - **Briefing:** The "Player's Manual" explaining concepts via RPG analogies.
    - **Lab:** The "Quest" to build a specific plugin folder (e.g., `src/plugins/m01_awakening`).
    - **Check:** The "System Diagnostic" to verify their code works.
    - **Template-First Labs:** Missions start from a prefilled `.py` template with comments and micro-tasks, so the learner edits and moves pieces instead of building from scratch.
    - **Black-Box Framework:** Treat `BasePlugin` as a contract, not a codebase to understand. Only explain the parts the learner touches.

## 2. The Pedagogy: "Coding is Minecraft"
We use **Minecraft/RPG analogies** to demystify "Boilerplate".
- **`import`** = **The Workbench**. Gathering tools from the shelf before crafting.
- **`class`** = **The Entity Type**. Defining a "Zombie" vs just a generic "Mob".
- **`Inheritance`** = **DNA**. "A Zombie *is a* Mob, but it groans."
- **`def` (Methods)** = **Abilities**. Special moves the entity can perform (e.g., `attack()`, `generate_image()`).
- **`self`** = **Me**. The entity pointing to its own chest. (e.g., "My health", "My texture").
- **Good vs Bad Examples:** Every key concept includes a tiny "bad vs good" exercise.
- **Use vs Avoid:** Learned through the `bad_code.py` fix + explanation, not a lecture section.
- **Surprise Factor:** Every mission ships one small, delightful surprise (font, visual effect, animation, or data reveal).

## 2.1 How We Teach Python (So It Sticks)
The goal is “useful outcome from day 1” without skipping fundamentals. The trick is to teach *only the next tool needed* to complete the mission, then reuse it across later missions until it becomes automatic.

**The 70/30 rule:** 70% building, 30% explanation. Keep explanations short, concrete, and immediately used.

### Mission Format (so an AI agent can generate materials)
Each Python mission should be written with these sections (in this order):
1. **Outcome (Visible Result)**: what changes on the screen / in the web UI.
2. **Concepts You Will Learn (List Only)**: list concepts without explanations.
3. **Glossary (with Examples)**: 5–10 terms with one-line definitions and a short example pointing to mission code.
4. **Briefing (Concept Explanations)**: Problem story → Solution → Before/after examples → Scalability context.
5. **Build (Steps)**: exact files to create/edit and the smallest slice that works.
6. **Practice (Inside the .py Template)**: TODOs in the mission `.py` file.
7. **Self-Learning Module**: `explain.md` (new example + line-specific questions), `debug_detective.md` (debugging challenge), `bad_code.py`, `bad_code_explain.md`.
   - Line-specific questions test pattern recognition, not memorization.
   - Removed `trace.md` (replaced by debugging challenges).
8. **Check (Acceptance Criteria)**: what “done” means; checklist + quick command.
9. **Surprise (The Wow Moment)**: listed in mission.md but implemented as a TODO in the `.py` template.
10. **Stretch (Optional)**: harder upgrades if motivation is high.
11. **Reflection (1–3 Questions)**: “What did you learn? What was tricky? What would you change?”

### Briefing Rule: Use Syntax Cards
Keep the RPG/Minecraft one-liner (memory hook), then immediately add a compact Syntax Card so the learner (and an AI agent) gets the missing “how does this syntax work?” details without turning the mission into a textbook.

Each **Syntax Card** must include:
1. **Hook** (1 line): the metaphor (“`def` = give your class an ability”).
2. **Definition** (1–2 sentences): what it really is in Python terms.
3. **Syntax card** (1 small snippet): show the pattern and label the parts.
4. **Common mistakes** (1–3 bullets): include what the error looks like.
5. **Where used in this mission**: point to the exact file/function.

**Use vs Avoid** should be taught via the `bad_code.py` exercise, not a standalone section.

### Core Syntax Cards Library (Project Standard)
These should be taught across missions (not all at once). Reuse the same wording/snippets to build muscle memory.

- **Functions & Return**: `def`, parentheses, parameters, indentation blocks, `return`.
- **Methods & `self`**: what `self` is, why it’s first, how calls work (`obj.method(...)`).
- **Calls vs Definitions**: defining a function vs calling it, arguments vs parameters.
- **Imports & Modules**: `import x` vs `from x import y`, where modules come from.
- **Types & Values**: `str/int/float/bool/None`, conversion, simple type errors.
- **Dictionaries**: literals `{}`, indexing `d["k"]`, safe access `d.get("k", default)`.
- **Lists & Loops**: list literals `[]`, indexing, `for item in items`, `range`.
- **Conditionals**: `if/elif/else`, comparisons, boolean logic.
- **Exceptions**: `try/except`, raising `RuntimeError` for user-facing plugin errors.
- **Files & JSON**: `open(...)`, read/write text, `json.load/dump` (when caching/settings appear).

### Borrowing from “30 Days of Python” (Recommended Policy)
Use it as a **coverage checklist** and an **optional deep-dive**, not the primary structure.

- Each mission should include only the Syntax Cards needed to finish the mission.
- Optionally add a short “If you want more” link to the relevant 30-Days topic page for the learner to read after the win.

### The “Python Toolkit” We Intentionally Cover
These are the “must learn” topics we’ll cover, but always through missions:
- Types and values (`str`, `int`, `float`, `bool`, `None`)
- Strings + formatting (f-strings)
- Collections (`list`, `dict`, `tuple`, `set` when useful)
- Control flow (`if`, `for`, `while`)
- Functions (parameters, return values)
- Modules + imports (project structure)
- Exceptions (`try/except`, raising `RuntimeError`)
- Reading/writing files (text + JSON)
- HTTP + JSON APIs (`requests`)
- Debugging habits (print/logging, reading tracebacks)
- Basic OOP (classes + inheritance via `BasePlugin`)

---

## 3. The Curriculum

### Phase 1: The System Engineer (Linux & Service)
*Focus: Demystifying the Creature. Understanding that "Hardware is just a File".*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-01** | **The Commander**<br>*"Remote Control."* | You are already using SSH, but what is it? We will learn how to securely enter the machine. | **SSH**: Secure Shell (Tunneling).<br>**Permissions**: `chmod +x` (Who is allowed to run this?).<br>**Network**: IP Intefaces, localhost vs 0.0.0.0. |
| **M-02** | **The Detective**<br>*"Why did it crash?"* | You typed `journalctl` blindly. Now we learn to actually *read* the diary of the machine. | **Journalctl**: Reading system logs.<br>**Grep**: Searching for "Error" in the stack.<br>**Streams**: Standard Output (stdout) vs Errors (stderr). |
| **M-03** | **The Alchemist**<br>*"Control hardware without code."* | How does software touch the physical world? In Linux, there is no magic. Hardware is just a file. | **File-System Hardware**: `/sys/class/leds`.<br>**Redirection**: `echo 1 > brightness`.<br>**Reading Sensors**: `cat /sys/class/thermal`. |
| **M-04** | **The Mechanic**<br>*"Stress test the engine."* | Resources are finite. A good engineer knows how to manage the "weight" of their code on the RAM. | **Processes**: PIDs and `htop`.<br>**Signals**: `kill -9` (The Termination Signal).<br>**Memory**: Physical RAM vs Swap. |
| **M-05** | **The Ghost**<br>*"Run on boot."* | The project runs automatically. How? We won't just use it; we will break it and fix it. | **Systemd**: `inkypi.service` file analysis.<br>**Daemons**: Background processes vs Foreground.<br>**Services**: `start`, `stop`, `enable`. |
| **B-01** | **BOSS BATTLE: The Scavenger Hunt**<br>*"Find the Hidden Files"* | **Challenge**: Hide a file deep in the system, create a service that writes a secret code to logs, and find it using `grep`.<br>*No Guide. Just Linux mastery.* | *Consolidating Navigation, Services, Logs, and Process Management.* |

### Phase 2: The Operator (Basics & Output)
*Focus: Understanding the environment, Objects, and the "Canvas".*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-06** | **The Awakening**<br>*"Wake up the machine."* | To make the hardware speak, we need to create a driver (Plugin) that controls the pixels. | **The Shell**: `mkdir`, code structure.<br>**The Blueprint**: `class` (Defining a new Entity).<br>**The DNA**: `inheritance` (Using templates).<br>**The Ability**: `def` (The specific task). |
| **M-07** | **The Timekeeper**<br>*"Fix the broken clock."* | The screen is static. We need variables that change value over time to show the present moment. | **Imports**: `datetime` module.<br>**Variables**: Capturing state.<br>**f-strings**: Injecting variables into text.<br>**Types**: `str` vs `int`. |
| **C-01** | **The Display Gallery**<br>*"Mini art wall."* | Build confidence by arranging simple shapes and labels on the screen. | **Variables**: Naming values.<br>**Coordinates**: Consistent layout.<br>**Types**: `int` vs `str` usage. |
| **C-02** | **The Creature Card**<br>*"Your pet on a card."* | Introduce class, object, and properties with a friendly, visible output. | **Class/Object**: Blueprint vs instance.<br>**Properties**: Stored facts.<br>**Methods**: Actions that draw. |
| **C-03** | **The Inheritance Practice**<br>*"Specialize a base card."* | Practice `super()` and extending a base class without touching framework internals. | **Base class**: Common behavior.<br>**Constructor**: Setup time.<br>**super()**: Ask the parent for help. |
| **M-08** | **The Artist**<br>*"Draw your gamer tag."* | Text is boring. We want graphics. We need to understand the X,Y grid to place pixels. | **Objects**: Creating a `Draw` object.<br>**Methods with Args**: Passing parameters.<br>**Tuples**: Grouping data like Colors (R,G,B).<br>**Coordinates**: Top-Left (0,0). |
| **B-02** | **BOSS BATTLE: The ID Card**<br>*"Digital Badge"* | **Challenge**: distinct layers (Photo, Name, Rank) combined into one image.<br>*No Guide. Pure creation.* | *Consolidating Class structure, Imports, Variables, and Drawing methods.* |

#### M-06 Mission Spec: The Awakening
**Outcome (Visible Result)**: A new plugin appears in the web UI and can render a simple “Hello, \<Name\>” card to the display.

**Build (Smallest Slice that Works)**
- Start from a prefilled `m06_awakening.py` template (commented step-by-step).
- Create plugin folder: `src/plugins/m06_awakening/`
- Create: `src/plugins/m06_awakening/plugin-info.json` (id + display name + class)
- Move the prefilled `m06_awakening.py` into `src/plugins/m06_awakening/`
  - `class Awakening(BasePlugin):`
  - implement `generate_image(self, settings, device_config)` using Pillow:
    - `Image.new(...)`, `ImageDraw.Draw(img)`, `draw.text(...)`
  - return a single `PIL.Image`
- Add an `icon.png` (can temporarily copy an existing icon).

**Teach (Concepts: micro-lessons)**
- `import`: “bring tools into this file” (show `from PIL import Image, ImageDraw`).
- `class` + inheritance: “your plugin *is a* `BasePlugin`”.
- Pillow: a library that creates and draws images for the e-ink display.
- Method signature: parameters, `self`, and return value.
- Strings: simple f-string: `f"Hello, {name}!"`.
- “Fail loudly”: when a required setting is missing, `raise RuntimeError("...")`.

**Practice (Tiny Exercises)**
- Change background color; change text color.
- Move text by changing X/Y numbers; describe what `(0, 0)` means.
- Add a border rectangle.

**Check (Acceptance Criteria)**
- Plugin appears under Plugins in the web UI.
- Generating an image does not crash; the result is visible on screen.

**Stretch**
- Add a `settings.html` textbox for the name; prepopulate when editing.
- Add “frame styles” by enabling style settings later.

**Reflection**
- What does `generate_image` return?
- What happens if you forget `return img`?

#### M-07 Mission Spec: The Timekeeper
**Outcome (Visible Result)**: The plugin shows the current time (and optionally date) and updates correctly after refresh.

**Build**
- Extend the M-06 plugin (or make `src/plugins/m07_timekeeper/`) to:
  - `from datetime import datetime`
  - read timezone config from device settings (or start with local time)
  - format text with f-strings

**Teach**
- Variables: “a name for a value” (e.g., `now = datetime.now()`).
- Types: numbers vs strings; why you can’t add them without conversion.
- Formatting: `strftime` (or minimal string slicing) and f-strings.

**Practice**
- Display seconds; then remove seconds and explain “why easier to read”.
- Show 12h vs 24h time with a setting toggle.

**Check**
- Time displayed matches real time (within 1 minute).

#### M-08 Mission Spec: The Artist
**Outcome**: A plugin draws a small “tag art” scene: name + one simple shape pattern.

**Build**
- Use Pillow drawing primitives:
  - `draw.rectangle`, `draw.rounded_rectangle` (if available), `draw.line`, `draw.circle` (or `ellipse`)
- Compute positions from display width/height, not hard-coded pixel magic.

**Teach**
- Coordinates: origin at top-left, X rightwards, Y downwards.
- Tuples: `(x, y)` and `(r, g, b)` grouping.
- Functions: write helpers like `draw_centered_text(draw, ...)` to avoid repetition.

**Practice**
- Draw 3 evenly spaced dots using a loop (sneak in `for` early).
- Change “magic numbers” to named variables.

**Check**
- Art scales: it still looks OK on different resolutions/orientations.

#### B-02 Boss Battle: The ID Card
**Outcome**: A “badge” plugin: photo (or placeholder block) + name + rank + QR code (optional).

**Teach**
- Composition: layers and ordering (background first).
- File paths: read a local image file safely.
- Dictionaries: represent “profile data” like `{"name": "...", "rank": "..."}`.

**Stretch**
- Add settings for name/rank/photo; persist choices via plugin settings.

### Phase 3: The Data Harvester (Data & APIs)
*Focus: Fetching the world's information and showing it.*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-09** | **The Inspector**<br>*"Show RAM/CPU usage."* | The machine has a heartbeat. We can read it using system dictionaries. | **Dictionaries**: Key/Value pairs.<br>**Accessing Data**: `stats['cpu']`.<br>**Libraries**: Using 3rd party tools (`psutil`). |
| **M-10** | **The Forecaster**<br>*"Build a weather station."* | The world is full of data. APIs let us ask "What is the weather?" and get a JSON answer. | **APIs**: `requests.get()` (Calling a phone number).<br>**JSON**: Understanding nested data structures.<br>**Keys**: Keeping secrets (API Keys) safe. |
| **M-11** | **The Tracker**<br>*"Watch Crypto/Stocks."* | We have too much data. We need to filter lists to find just the one item we care about. | **Lists**: Ordered collections.<br>**Indexing**: `prices[0]`.<br>**Float Math**: Decimal math. |
| **B-03** | **BOSS BATTLE: The Dashboard**<br>*"3-Panel Info Cycle"* | **Challenge**: Fetch Weather AND Hardware stats, display side-by-side.<br>*Managing multiple data sources and complex layout.* | *Consolidating Dictionaries, APIs, Lists, and Layout logic.* |

#### M-09 Mission Spec: The Inspector
**Outcome**: A plugin shows CPU/RAM/disk usage with simple bars or numbers.

**Build**
- Read data (preferred): `psutil` (already used in many Pi projects).
- Convert raw numbers to human-friendly strings (percentages, MB/GB).
- Render: text + a simple bar chart rectangle.

**Teach**
- Dictionaries: `stats = {"cpu": 23, "ram": 41}` and `stats["cpu"]`.
- Functions: `get_stats()` returns a dict; `format_bytes(n)` returns a string.
- “Defensive coding”: missing keys; fallback values.

**Practice**
- Add temperature reading from `/sys/class/thermal/...` as a stretch sensor.
- Color the bar red when usage > 80% (introduce `if` early).

#### M-10 Mission Spec: The Forecaster
**Outcome**: Weather plugin-lite: shows current temperature + condition icon/text for your location.

**Build**
- Use `requests.get(...)` to call a weather API.
- Parse JSON response into a small internal dict: `{"temp": ..., "condition": ...}`
- Handle errors: no network, bad API key, unexpected JSON shape.

**Teach**
- HTTP requests: “call a URL, get a response”.
- JSON as nested dict/list structures.
- Secrets: API keys belong in env/config, not hard-coded in code.
- Exceptions: `try/except` around network and parsing; raise `RuntimeError` with user-friendly message.

**Practice**
- Add a “last updated” timestamp.
- Cache data in `settings` (simple persistence) so the plugin can display the last known value if the network fails.

#### M-11 Mission Spec: The Tracker
**Outcome**: Shows a tracked item (stock/crypto) and change (up/down) with a tiny arrow.

**Build**
- Fetch a list of prices/quotes from an API.
- Find the item by symbol using:
  - a loop, then later a list comprehension.
- Display formatted numbers and a change indicator.

**Teach**
- Lists: order, indexing, iterating.
- Filtering: `for item in items:` and `if item["symbol"] == target:`
- Float formatting: rounding, and why money formatting matters.

**Practice**
- Track 2 symbols and render the one with the biggest move.
- Sort a list by a field (`sorted(items, key=...)`).

#### B-03 Boss Battle: The Dashboard
**Outcome**: One plugin combines 2–3 panels (e.g., time + weather + system stats).

**Teach**
- Decomposition: split into functions like `draw_header(...)`, `draw_weather(...)`.
- Layout: define rectangles for each panel; draw inside boundaries.
- “Data pipeline”: fetch → parse → render (keep these separate).

### Phase 4: The Architect (Logic & Control)
*Focus: Making the system smart and autonomous.*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-12** | **The Night Watch**<br>*"Auto Dark Mode."* | The screen is too bright at night. The code must *decide* which colors to use based on time. | **Conditionals**: `if/else` (Making decisions).<br>**Booleans**: `True` / `False`.<br>**Comparison**: `>`, `<`, `==`. |
| **M-13** | **The Looper**<br>*"Countdown Timer."* | We need to count down from 10. Writing a print statement 10 times is stupid. Loops let us repeat. | **Loops**: `for i in range(10):`.<br>**While Loops**: `while active:`.<br>**Sleep**: `time.sleep()`. |
| **M-14** | **The Guardian**<br>*"Crash Protection."* | Sometimes the internet fails. The program should not die; it should handle the error. | **Exceptions**: `try:` / `except:` (Safety nets).<br>**Scope**: Local vs Global variables.<br>**Logging**: Proper error tracking. |
| **B-04** | **BOSS BATTLE: The Smart Frame**<br>*"Context Aware Display"* | **Challenge**: If Wifi is down -> Show Clock. If Wifi is up -> Show Weather.<br>*Complex logic trees.* | *Consolidating Control Flow, Error Handling, and State.* |

#### M-12 Mission Spec: The Night Watch
**Outcome**: The plugin switches theme (light/dark) automatically based on time.

**Teach**
- Booleans and comparisons.
- `if/elif/else` decision trees.
- Keep “policy” separate from “rendering”: compute `theme` first, then draw.

#### M-13 Mission Spec: The Looper
**Outcome**: A countdown or progress animation (within a single render) OR a “step” counter that changes each refresh.

**Teach**
- `for` loops and `range`.
- `while` loops only if needed (avoid infinite loop mistakes early).
- Time: `sleep` conceptually (but don’t freeze the whole service in production).

**Coach Note**: In InkyPi, plugins are expected to render and return an image quickly. Use loops for drawing repeated shapes, not long-running timers.

#### M-14 Mission Spec: The Guardian
**Outcome**: The plugin never “hard crashes” on common failures; it shows a friendly error screen instead.

**Teach**
- Tracebacks: how to read the last line first.
- `try/except` around the smallest risky block.
- Raising `RuntimeError` for clean UI errors.
- Logging: `logger.info(...)`, `logger.warning(...)`, `logger.exception(...)`.

#### B-04 Boss Battle: The Smart Frame
**Outcome**: Context-aware display:
- If internet OK → Weather
- If internet down → Clock
- If disk almost full → Warning screen

**Teach**
- Priorities: order conditions; don’t let multiple branches fight.
- “Fallback strategy”: always have a safe default output.

---

## Appendix A: Mapping “30 Days of Python” Topics to Missions
This is not a replacement for that course; it’s a coverage map so we don’t miss fundamentals.

- Intro / Setup / Running code → Phase 1 + M-06 scaffolding
- Variables, Types, Casting → M-07, M-09
- Strings + formatting → M-06, M-07
- Lists / loops → M-11, M-13
- Tuples → M-08 (coords/colors)
- Dictionaries → M-09, M-10
- Conditionals → M-12
- Functions → M-08, B-03
- Modules → M-06 onward (imports + project structure)
- Exceptions → M-10, M-14
- File handling → B-02 (assets), optional caching in M-10
- APIs / JSON → M-10, M-11

## Appendix B: Coach Checklist (Keep Motivation High)
- Start each session with a **demo of the goal** (30 seconds).
- Timebox “stuck time”: if blocked for 5–10 minutes, switch to a hint.
- Always end with a **visible win** (even a small one): a new icon, a new panel, a new setting.
- Keep a “victory log”: screenshot the display after each mission.


#Geneate mission using AI, Prompt:
I want to create mission C-04 (List Practice).
Follow the QUICK_START.md guide in _mission_templates_syllabus.
Use templates 1-4 in order to generate all mission files.