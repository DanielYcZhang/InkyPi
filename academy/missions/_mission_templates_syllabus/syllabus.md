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

| ID | Title & Hook | Est. Time | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :---: | :--- | :--- |
| **M-06** | **The Awakening**<br>*"Wake up the machine."* | 1.5h | To make the hardware speak, we need to create a driver (Plugin) that controls the pixels. | **The Shell**: `mkdir`, code structure.<br>**The Blueprint**: `class` (Defining a new Entity).<br>**The DNA**: `inheritance` (Using templates).<br>**The Ability**: `def` (The specific task). |
| **M-07** | **The Timekeeper**<br>*"Fix the broken clock."* | 1.5h | The screen is static. We need variables that change value over time to show the present moment. | **Imports**: `datetime` module.<br>**Variables**: Capturing state.<br>**f-strings**: Injecting variables into text.<br>**Types**: `str` vs `int`. |
| **C-01** | **The Display Gallery**<br>*"Mini art wall."* | 2h | Build confidence by arranging simple shapes and labels on the screen. Master layout fundamentals. | **Variables**: Naming values for reuse.<br>**Coordinates**: X,Y positioning.<br>**Loops**: Repeat without copy-paste.<br>**DRY Principle**: One change updates all. |
| **C-02** | **The Creature Card**<br>*"Your pet on a card."* | 2h | Introduce class, object, and properties with a friendly, visible output. | **Class/Object**: Blueprint vs instance.<br>**Properties**: Stored facts (`self.name`).<br>**Methods**: Actions that draw.<br>**Encapsulation**: Data + behavior together. |
| **C-03** | **The Inheritance Practice**<br>*"Specialize a base card."* | 2h | Practice `super()` and extending a base class. Master code reuse through inheritance. | **Base class**: Common behavior.<br>**Inheritance**: IS-A relationship.<br>**super()**: Reusing parent's code.<br>**Polymorphism**: Different types, same interface. |
| **C-04** | **The Code Detective**<br>*"How does InkyPi work?"* | 2h | You've built 5 plugins. But how does the system actually CALL your code? Time to read production code. | **Code Reading**: Tracing imports & calls.<br>**Architecture**: Request → Plugin → Display flow.<br>**Contracts**: Why BasePlugin is an interface.<br>**System Thinking**: Understanding the bigger picture. |
| **M-08** | **The Anime Gallery**<br>*"Display your favorite character."* | 2h | Text is cool, but images are better! Load and display anime character art on your wall. | **File I/O**: Reading image files.<br>**PIL Image Loading**: `Image.open()`.<br>**Image Operations**: Resize, paste, composite.<br>**File Paths**: Relative vs absolute paths. |
| **B-02** | **BOSS BATTLE: The Character Showcase**<br>*"Rotating anime art display"* | 3h | **Challenge**: Build a plugin that cycles through multiple character images with names and info cards.<br>*Managing collections, file organization, and layout.* | *Consolidating File I/O, Lists, Layout, and Image Composition.* |

---

### Phase 2.5: Building Real Features (Student-Driven Projects)
*Focus: Integrating with real services, solving personal problems, product thinking.*

| ID | Title & Hook | Est. Time | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :---: | :--- | :--- |
| **M-09** | **The Spotify Connector**<br>*"What's playing right now?"* | 2h | You listen to music on your Mac. Let's show the current track and album cover on your wall! | **APIs**: HTTP requests to external services.<br>**OAuth**: Authentication tokens (simplified).<br>**JSON**: Parsing API responses.<br>**Error Handling**: What if Spotify is offline? |
| **M-10** | **The Album Artist**<br>*"Beautiful cover art."* | 2h | Make your Spotify display look AMAZING. Download album covers, cache them, handle missing artwork gracefully. | **Image Download**: Fetching from URLs.<br>**Caching**: Save images locally to avoid re-downloading.<br>**Fallbacks**: Default image when album art missing.<br>**Product Thinking**: User experience matters. |
| **M-11** | **The Anime Quote**<br>*"Daily wisdom from Demon Slayer."* | 1.5h | Display rotating quotes from your favorite anime characters. Learn list operations and text wrapping. | **Lists**: Collections of quotes.<br>**Random Selection**: `random.choice()`.<br>**Text Wrapping**: Multi-line formatting.<br>**Data Organization**: Quote + character + source. |
| **C-05** | **Lists & Loops Practice**<br>*"Master the collection."* | 2h | Practice lists, loops, and iteration through focused exercises. Build a todo list display. | **List Operations**: append, remove, index.<br>**For Loops**: Iterating collections.<br>**Enumerate**: Getting index + item.<br>**List Comprehensions**: Filtering & transforming. |
| **M-12** | **The Stats Dashboard**<br>*"System health at a glance."* | 2h | Display CPU, RAM, disk usage with visual bars. Learn dictionaries and data visualization. | **Dictionaries**: Key-value pairs.<br>**External Libraries**: `psutil` for system stats.<br>**Data Formatting**: Bytes to GB, percentages.<br>**Visual Encoding**: Numbers to bar lengths. |
| **B-03** | **BOSS BATTLE: The Personal Dashboard**<br>*"Everything in one view"* | 3h | **Challenge**: Combine Spotify + System Stats + Anime Quote in one smart display.<br>*Layout planning, data integration, error resilience.* | *Consolidating APIs, Layouts, Error Handling, Product Design.* |

---

### Phase 3: The Engineer (Logic, Control & Debugging)
*Focus: Making systems intelligent, resilient, and maintainable.*

| ID | Title & Hook | Est. Time | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :---: | :--- | :--- |
| **M-13** | **The Smart Switcher**<br>*"Auto-change based on time."* | 2h | At night, show anime scenes. In the morning, show your schedule. Teach the display to DECIDE. | **Conditionals**: `if/elif/else` decision trees.<br>**Time Logic**: Hour-based decisions.<br>**Booleans**: True/False logic.<br>**State Machines**: Different modes. |
| **M-14** | **The Music Historian**<br>*"Track your listening stats."* | 2h | Keep a history of what you played on Spotify. Display your top artists/songs this week. | **Data Persistence**: Writing to JSON files.<br>**File Append**: Adding to history.<br>**Aggregation**: Counting occurrences.<br>**Sorting**: Top 5 most played. |
| **M-15** | **The Guardian**<br>*"Never crash again."* | 2h | APIs fail. Images disappear. The internet drops. Make your plugins BULLETPROOF. | **Exception Handling**: `try/except` blocks.<br>**Logging**: Recording what happened.<br>**Graceful Degradation**: Show something even when things fail.<br>**Debugging**: Reading stack traces. |
| **C-06** | **Functions & Modularity Practice**<br>*"Clean code structure."* | 2h | Your code is getting messy. Learn to organize with functions and modules. | **Functions**: Reusable code blocks.<br>**Parameters & Returns**: Input/output contracts.<br>**Module Organization**: Splitting code into files.<br>**DRY at Scale**: Eliminating all duplication. |
| **M-16** | **The Scene Selector**<br>*"Anime moments on demand."* | 2h | Build a plugin that lets you CHOOSE which anime scene to display through web UI settings. | **Settings UI**: HTML forms for configuration.<br>**User Input**: Dropdowns, text fields.<br>**Dynamic Behavior**: Code adapts to user choices.<br>**Product Thinking**: Building for users, not just yourself. |
| **B-04** | **BOSS BATTLE: The Smart Display**<br>*"Context-aware system"* | 3h | **Challenge**: Display changes based on context:<br>- Playing music → Spotify<br>- Not playing → Anime quote<br>- Low battery (if detectable) → System stats warning<br>*Complex conditional logic, multi-source data, fallback strategies.* | *Consolidating Logic, State Management, Error Handling, System Integration.* |

---

### Phase 4: The Architect (Advanced Integration & Polish)
*Focus: Building production-quality features, advanced integrations, collaboration.*

| ID | Title & Hook | Est. Time | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :---: | :--- | :--- |
| **M-17** | **The Collaborator**<br>*"Code review practice."* | 2h | Read a teammate's plugin code (simulated). Add a feature to someone else's code. Learn collaboration. | **Code Reading**: Understanding others' logic.<br>**Documentation**: Writing clear comments.<br>**Git Basics**: Branches, commits (introduction).<br>**Code Style**: Consistency matters. |
| **M-18** | **The Anime Recommender**<br>*"Discover new shows."* | 2.5h | Integrate with an anime API (MyAnimeList, AniList). Display top-rated shows, search for similar anime. | **Advanced APIs**: Authentication, pagination.<br>**Data Filtering**: Finding relevant results.<br>**Rate Limiting**: Respecting API quotas.<br>**Async Thinking**: API calls take time. |
| **M-19** | **The Music Mood**<br>*"Visualize your vibe."* | 2.5h | Analyze Spotify track features (energy, tempo, mood). Display a visual representation of your current music vibe. | **Data Analysis**: Working with numerical data.<br>**Normalization**: Scaling values to visual ranges.<br>**Color Mapping**: Numbers to colors.<br>**Algorithm Design**: Mood calculation logic. |
| **C-07** | **Testing & Debugging Practice**<br>*"Professional reliability."* | 2h | Learn to write tests, debug systematically, and handle edge cases like a professional engineer. | **Unit Tests**: Testing individual functions.<br>**Test-Driven Development**: Write tests first.<br>**Debugging Workflow**: Hypothesis → Test → Fix.<br>**Edge Cases**: Null, empty, extreme values. |
| **M-20** | **The Portfolio Showcase**<br>*"Your best work on display."* | 2h | Build a plugin that cycles through your best creations. Screenshot-worthy display of your journey. | **Reflection**: Review what you've built.<br>**Composition**: Combining multiple features.<br>**Polish**: Making it screenshot-worthy.<br>**Pride**: Celebrating your growth. |
| **B-05** | **FINAL BOSS: The Ultimate Display**<br>*"Your masterpiece"* | 4h | **Challenge**: Design and build YOUR ultimate InkyPi plugin. Could be:<br>- Spotify + Anime hybrid<br>- Interactive game<br>- Multi-panel dashboard<br>- Your own idea!<br>*Complete creative freedom. Show everything you've learned.* | *Demonstrating Mastery: Architecture, APIs, UI, Error Handling, Product Thinking, Clean Code.* |

---

#### Detailed Mission Specs (Updated)

##### C-04 Mission Spec: The Code Detective
**Outcome (Visible Result)**: A system architecture diagram (drawn or described in markdown) showing how a web request becomes a displayed image.

**Build (Guided Code Tour)**
1. **Start from the Web UI**:
   - Find the "Generate Image" button in the web interface
   - Trace which Python file handles this HTTP endpoint
   - Follow: `web route → plugin_manager → your plugin`

2. **Understand Plugin Discovery**:
   - Open `plugin_manager.py` (or equivalent)
   - Find code that loads `plugin-info.json` files
   - Question: "How does InkyPi know your plugin exists?"

3. **Read BasePlugin Contract**:
   - Open `BasePlugin` source code
   - Identify the "contract" (which methods MUST be implemented)
   - Compare to your C-02 CreatureCard - where do they match?

4. **Tr device_config Flow**:
   - Find where `device_config` comes from
   - Trace: Where does screen resolution get determined?
   - Why does your plugin receive this object?

5. **Follow Image Rendering**:
   - After `generate_image()` returns, what happens to the PIL Image?
   - How does Python image → e-ink display?
   - Find the code that writes to hardware

**Teach (Code Reading Skills)**
- **Finding Definitions**: Use IDE "Go to Definition" or `grep`
- **Tracing Calls**: Work backwards from your code to the system
- **Understanding Imports**: What does `from ...base_plugin import BasePlugin` mean?
- **Interfaces vs Implementations**: BasePlugin defines contract, you implement
- **Reading Without Running**: Understanding code by reading (like reading a blueprint)

**Practice (Detective Work)**
- Find: "Where is `plugin-info.json` loaded?"
- Find: "What calls the `generate_image()` method?"
- Find: "How does the system handle plugin errors?"
- Trace: Complete flow from web UI click to display update

**Deliverable**
Create `c04_architecture.md` with:
1. Diagram (ASCII art or description) of the complete flow
2. Answers to 5 detective questions
3. "Aha!" moments: 3 things you learned about the system

**Check (Acceptance Criteria)**
- Diagram shows: Web UI → Routes → PluginManager → YourPlugin → Image → Display
- Can explain: "What is BasePlugin's purpose?"
- Can trace: From button click to screen update
- Understand: You're part of a larger system!

**Reflection**
- What surprised you about InkyPi's design?
- How would you explain BasePlugin to someone new?
- What part of the code was hardest to understand? Why?

**Time Estimate**: 2 hours
- 30 min: Setup + understand the goals
- 60 min: Guided code tour with questions
- 30 min: Create diagram + write up findings

---

##### M-08 Mission Spec: The Anime Gallery
**Outcome (Visible Result)**: Display your favorite anime character (e.g., Tanjiro from Demon Slayer) with name and series info.

**Build**
1. Create `src/plugins/m08_anime_gallery/`
2. Download or find a character image (Tanjiro, Nezuko, etc.)
3. Learn to load image files with PIL:
   ```python
   from PIL import Image
   character_img = Image.open("path/to/tanjiro.png")
   ```
4. Resize image to fit screen
5. Composite character image onto background
6. Add text overlay: character name + series

**Teach (Image Fundamentals)**
- **File Paths**: Where to store images (project structure)
- **Image.open()**: Loading external images
- **Resize**: `img.resize((width, height))`
- **Paste/Composite**: Layering images
- **Image Modes**: RGB vs RGBA (transparency)

**Practice**
- Change which character displays
- Add a border around the character
- Position character left, center, or right
- Add quote below character

**Surprise**
Hidden feature: Add transparency support so character cutouts look clean!

**Stretch**
- Create a folder of multiple characters
- Randomly select one each refresh
- Add character stats (rank, breathing style, etc.)

**Check**
- Character image displays clearly
- Name and series text visible
- Image properly sized for screen
- No crashes when image file missing (graceful error)

**Reflection**
- What's the difference between `Image.new()` and `Image.open()`?
- Why do we resize images before displaying?
- How would you add a second character?

**Time Estimate**: 2 hours

---

##### M-09 Mission Spec: The Spotify Connector
**Outcome (Visible Result)**: Display current playing track name and artist from your Mac's Spotify.

**Build**
1. Set up Spotify API credentials (simplified, use existing token if possible)
2. Make first API request: `GET current-playing`
3. Parse JSON response:
   ```python
   track_name = data["item"]["name"]
   artist = data["item"]["artists"][0]["name"]
   ```
4. Display on e-ink: "Now Playing: {track_name} by {artist}"
5. Handle case: Nothing playing → show "No music playing"

**Teach (API Fundamentals)**
- **APIs as Phone Numbers**: You call Spotify, it answers with data
- **HTTP GET**: Asking for information
- **JSON Structure**: Nested dictionaries and lists
- **Authentication**: API tokens (use environment variables)
- **Error Handling**: What if Spotify says "no"?

**The "Aha!" Moment**
When you **play a song on your Mac** and it shows up on the display - that's when it clicks that systems can talk to each other!

**Practice**
- Display track duration
- Show if it's playing or paused
- Add album name
- Handle long text (truncate or wrap)

**Check**
- Playing a song → plugin shows correct track
- Stopping playback → plugin shows fallback message
- Wrong credentials → clear error message (not crash)

**Stretch**
- Set up automatic refresh (every 30 seconds)
- Add progress bar showing play position

**Reflection**
- What does the JSON response look like?
- What happens if the internet is down?
- How often should we check "what's playing"?

**Time Estimate**: 2 hours
- 30 min: API setup + credentials
- 60 min: Making requests, parsing JSON
- 30 min: Error handling + polish

---

##### M-10 Mission Spec: The Album Artist
**Outcome (Visible Result)**: Display beautiful album cover art alongside track info.

**Build**
1. Get album artwork URL from Spotify API response
2. Download image from URL:
   ```python
   import requests
   response = requests.get(artwork_url)
   img = Image.open(BytesIO(response.content))
   ```
3. Cache downloaded images (save to disk)
4. Composite: Album art (left) + Track info (right)
5. Fallback: Default "no artwork" image

**Teach (Advanced Image Handling)**
- **Downloading Images**: `requests.get()` for binary data
- **BytesIO**: In-memory file handling
- **Caching Strategy**: Save to avoid re-downloading
- **File Naming**: Hash or album_id for filenames
- **Composition**: Layouts with multiple elements

**The "Aha!" Moment**
Seeing YOUR CURRENT SONG's album cover on your wall - that's magical! The display becomes a **living music companion**.

**Practice**
- Make album art larger or smaller
- Blur background, sharp foreground
- Add colored border matching album's dominant color
- Round corners on artwork

**Check**
- Album art displays for current track
- Missing artwork → shows default image
- Downloaded images cached (don't re-download)
- Layout looks good (not stretched/distorted)

**Stretch**
-Clean old cache (keep only 50 most recent albums)
- Add dominant color extraction for themed background

**Reflection**
- Why cache images? What's the benefit?
- What happens if artwork URL is broken?
- How much disk space could cached images use?

**Time Estimate**: 2 hours

---

##### M-11 Mission Spec: The Anime Quote
**Outcome (Visible Result)**: Display rotating quotes from Demon Slayer characters.

**Build**
1. Create list of quotes:
   ```python
   quotes = [
       {"text": "Never give up!", "character": "Tanjiro", "series": "Demon Slayer"},
       {"text": "Mmmph mmmph!", "character": "Nezuko", "series": "Demon Slayer"},
       # ... more quotes
   ]
   ```
2. Random selection: `import random; quote = random.choice(quotes)`
3. Text wrapping for long quotes
4. Display: Quote text (large) + Character name (small) + Series

**Teach (Lists & Data Structures)**
- **Lists**: Ordered collections `[]`
- **Dictionaries**: Structured data `{}`
- **Random Module**: `random.choice()`
- **Text Wrapping**: `textwrap` module for multi-line text
- **Data Organization**: Structuring related information

**Practice**
- Add 10 more quotes
- Filter quotes by character
- Display only quotes under certain length
- Add Japanese text (if display supports)

**Check**
- Each refresh shows a different quote
- Long quotes wrap properly (don't overflow)
- Character attribution clear
- At least 15 quotes in collection

**Stretch**
- Load quotes from external JSON file
- Theme quote by time of day (motivational morning, calm evening)
- Add character image next to quote

**Reflection**
- How do lists and random selection work together?
- How would you add user's favorite quotes?
- What's better: quotes in code or external file? Why?

**Time Estimate**: 1.5 hours

---

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

---

## Appendix A: Mapping "30 Days of Python" Topics to Missions
This is not a replacement for that course; it's a coverage map so we don't miss fundamentals.

**Updated Mapping (Redesigned Curriculum)**:
- Intro / Setup / Running code → Phase 1 + M-06 scaffolding
- Variables, Types, Casting → M-07 (Timekeeper), C-01 (Display Gallery)
- Strings + formatting → M-06, M-07 (f-strings)
- Classes + Objects → C-02 (Creature Card), C-03 (Inheritance Practice)
- Lists / loops → C-05 (Lists Practice), M-11 (Anime Quote)
- Tuples → C-01 (coordinates), M-10 (Album Artist - colors)
- Dictionaries → M-09 (Spotify JSON), M-12 (Stats Dashboard)
- Conditionals → M-13 (Smart Switcher)
- Functions → C-06 (Functions Practice), throughout all missions
- Modules → M-06 onward (imports + project structure), C-04 (Code Detective)
- Exceptions → M-09/M-10 (API failures), M-15 (The Guardian)
- File handling → M-08 (Anime Gallery - images), M-14 (Music Historian - JSON)
- APIs / JSON → M-09 (Spotify), M-10 (Album Art), M-18 (Anime Recommender)

---

## Appendix B: Software Engineering Concepts Covered

The redesigned curriculum explicitly teaches software engineering thinking:

### Code Reading & Architecture (C-04)
- Tracing code execution
- Understanding system architecture
- Reading production code
- Interface vs implementation

### Product Thinking (Throughout)
- M-09: User-driven feature (Spotify integration)
- M-10: User experience (beautiful album art, caching)
- M-16: Configuration UI (user choices)
- B-05: Complete creative freedom (own ideas)

### Error Handling & Resilience (M-15, throughout)
- Try/except blocks
- Graceful degradation
- Logging for debugging
- Fallback strategies

### Collaboration (M-17)
- Code review practice
- Reading others' code
- Documentation
- Code style consistency

### Debugging Workflow (C-07, M-15)
- Reading stack traces
- Hypothesis → Test → Fix
- Logging strategies
- Systematic debugging

### Design Patterns (Throughout)
- DRY principle (C-01, C-03)
- Separation of concerns (all missions)
- Caching (M-10)
- State management (M-13, M-14)

---

## Appendix C: Motivation Arc & Student Engagement

**Evidence of Engagement**:
- Student suggested Spotify integration (owns the project!)
- Interest in anime/cartoons (natural motivation)
- Completed C01-C03 successfully

**Designed Motivation Triggers**:

1. **Personal Relevance** (Every Mission):
   - M-08: Display YOUR favorite character
   - M-09: Show what YOU'RE listening to
   - M-11: Quotes from anime YOU watch
   - M-19: Visualize YOUR music mood

2. **Immediate Gratification**:
   - Each mission = visible output on wall
   - 2-hour completion = same-day victory
   - Album cover appears when song plays = magical moment

3. **Creative Freedom Progression**:
   - Early: Guided missions with templates
   - Middle: Personal choices (which character, which quotes)
   - Late: Complete freedom (B-05: Your masterpiece)

4. **Social Proof**:
   - M-20: Portfolio showcase (show friends)
   - Screenshots of display throughout journey
   - B-05: Final project to share

---

## Appendix D: Coach Checklist (Keep Motivation High)

### Session Structure (Per Mission)
1. **Start with a demo** (30 seconds):
   - Show the end result first
   - Example: Play a song, show it appearing on display instantly
   - "This is what you'll build today"

2. **Set the timer** (2 hours):
   - "We're aiming to finish this in 2 hours"
   - Builds focus and urgency

3. **First checkpoint quick win** (15-30 min):
   - Hit CHECKPOINT 1 fast
   - "Plugin appears! Great start!"

4. **Mid-mission check-in** (60 min mark):
   - "How are you feeling? Stuck on anything?"
   - Provide hints if needed

5. **Celebrate completion**:
   - Screenshot the display
   - Add to victory log
   - "What's your favorite part?"

### Motivation Maintenance
- **Victory Log**: Screenshot display after each mission
- **Stuck Time Limit**: 5-10 minutes blocked → give hint
- **Visible Progress**: Can see all completed plugins on wall
- **Surprise Factor**: Hidden features in stretch goals
- **Next Mission Teaser**: "Next time, we'll make it BETTER..."

### When Motivation Dips
- **Pivot to interest**: If stuck on API, switch to anime images
- **Skip stretch goals**: Core mission = success
- **Show real-world**: "Spotify does this exact thing!"
- **Celebrate partial wins**: "The connection works! That's huge!"

---

## Appendix E: Time Estimates by Mission Type

| Mission Type | Est. Time | Complexity | Example |
|--------------|-----------|------------|---------|
| **Foundational (M-series)** | 1.5-2h | Low-Medium | M-06, M-07 |
| **Core Practice (C-series)** | 2h | Medium | C-01, C-02, C-03 |
| **Code Reading (C-04)** | 2h | Medium | C-04 only |
| **Integration** | 2h | Medium-High | M-09, M-10 |
| **Advanced** | 2-2.5h | High | M-18, M-19 |
| **Boss Battles** | 3-4h | High | B-02 to B-05 |

**Total Curriculum Time** (excluding Phase 1, already completed):
- Phase 2: ~14 hours (7 missions × 2h)
- Phase 2.5: ~12 hours (6 missions)
- Phase 3: ~12 hours (6 missions)
- Phase 4: ~13 hours (6 missions)
- Boss Battles: ~13 hours (5 battles)

**Total: ~64 hours** of focused learning with 30+ visible projects on the wall!

---

## Appendix F: AI Mission Generation Prompt Template

When using AI to generate a new mission from this syllabus:

```
I want to create mission [ID] ([Mission Name]).
Reference: /academy/missions/_mission_templates_syllabus/

Follow this process:
1. Read QUICK_START.md for the step-by-step workflow
2. Use templates 1-4 in order:
   - 1_briefing_template.md → Create briefing.md
   - 2_mission_md_template.md → Create mission.md
   - 3_self_learning_template.md → Create all self-learning files
   - 4_check_py_template.md → Create check.py

Mission Details from syllabus.md:
- ID: [e.g., M-09]
- Title: [e.g., "The Spotify Connector"]
- Estimated Time: [e.g., 2h]
- Core Concepts: [e.g., APIs, JSON, Error Handling]
- Student Motivation: [e.g., Show what's playing on Spotify]
- Visible Outcome: [e.g., Track name + artist on display]

Ensure:
- Problem-driven briefing (show pain without concept)
- 4 incremental checkpoints in mission.md
- Metrics-driven bad_code exercise (improvement ratios)
- Real-world examples (apps student uses)
- 2-hour time scope
```

---

## Summary: Why This Curriculum Works

**Aligns with All 3 Goals**:

1. **Motivation-driven learning** ✅
   - Student-suggested projects (Spotify)
   - Personal interests (anime)
   - Immediate gratification (visible on wall)
   - Progressive difficulty (GTA5-like flow)

2. **Outcome-driven** ✅
   - Every mission → new plugin
   - Physical display (not abstract)
   - 30+ tangible projects

3. **Python + Hardware mastery** ✅
   - Real Raspberry Pi integration
   - E-ink display constraints
   - System architecture (C-04)
   - Production-quality code

**Software Engineering Thinking**:
- Code reading (C-04)
- Architecture understanding (BasePlugin)
- Error handling (M-15)
- Product design (M-16)
- Collaboration (M-17)
- Testing/debugging (C-07)

**The Advantage**: Not just "learn Python" but "think like an engineer who builds real things."

Your son will finish with:
- 30+ working plugins
- Deep Python knowledge
- Hardware integration experience
- Portfolio to show friends
- **Most importantly**: The ability to BUILD HIS OWN IDEAS (Spotify display was his idea!)

That's when you know the curriculum succeeded - when he starts creating, not just completing.