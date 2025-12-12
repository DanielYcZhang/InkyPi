# InkyPi Academy Syllabus

## 1. The Strategy: "The Plugin Factory"
Instead of writing throwaway scripts, the student will build **Real InkyPi Plugins** for every mission.
- **The Context:** "You are an Engineer extending the capabilities of this device."
- **The Result:** Every mission ends with a permanent, usable feature on their wall.
- **The Delivery:**
    - **Briefing:** The "Player's Manual" explaining concepts via RPG analogies.
    - **Lab:** The "Quest" to build a specific plugin folder (e.g., `src/plugins/m01_awakening`).
    - **Check:** The "System Diagnostic" to verify their code works.

## 2. The Pedagogy: "Coding is Minecraft"
We use **Minecraft/RPG analogies** to demystify "Boilerplate".
- **`import`** = **The Workbench**. Gathering tools from the shelf before crafting.
- **`class`** = **The Entity Type**. Defining a "Zombie" vs just a generic "Mob".
- **`Inheritance`** = **DNA**. "A Zombie *is a* Mob, but it groans."
- **`def` (Methods)** = **Abilities**. Special moves the entity can perform (e.g., `attack()`, `generate_image()`).
- **`self`** = **Me**. The entity pointing to its own chest. (e.g., "My health", "My texture").

---

## 3. The Curriculum

### Phase 1: The System Engineer (Linux & Service)
*Focus: Demystifing the magic commands he already types.*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-01** | **The Commander**<br>*"Remote Control."* | You are already using SSH, but what is it? We will learn how to securely enter the machine. | **SSH**: Secure Shell (Tunneling).<br>**Permissions**: `chmod +x` (Who is allowed to run this?).<br>**Network**: IP Intefaces, localhost vs 0.0.0.0. |
| **M-02** | **The Detective**<br>*"Why did it crash?"* | You typed `journalctl` blindly. Now we learn to actually *read* the diary of the machine. | **Journalctl**: Reading system logs.<br>**Grep**: Searching for "Error" in the stack.<br>**Streams**: Standard Output (stdout) vs Errors (stderr). |
| **M-03** | **The Ghost**<br>*"Run on boot."* | The project runs automatically. How? We won't just use it; we will break it and fix it. | **Systemd**: `inkypi.service` file analysis.<br>**Daemons**: Background processes vs Foreground.<br>**Services**: `start`, `stop`, `enable`. |
| **B-01** | **BOSS BATTLE: The Scavenger Hunt**<br>*"Find the Hidden Files"* | **Challenge**: Hide a file deep in the system, create a service that writes a secret code to logs, and find it using `grep`.<br>*No Guide. Just Linux mastery.* | *Consolidating Navigation, Services, and Logs.* |

### Phase 2: The Operator (Basics & Output)
*Focus: Understanding the environment, Objects, and the "Canvas".*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-04** | **The Awakening**<br>*"Wake up the machine."* | To make the hardware speak, we need to create a driver (Plugin) that controls the pixels. | **The Shell**: `mkdir`, code structure.<br>**The Blueprint**: `class` (Defining a new Entity).<br>**The DNA**: `inheritance` (Using templates).<br>**The Ability**: `def` (The specific task). |
| **M-05** | **The Timekeeper**<br>*"Fix the broken clock."* | The screen is static. We need variables that change value over time to show the present moment. | **Imports**: `datetime` module.<br>**Variables**: Capturing state.<br>**f-strings**: Injecting variables into text.<br>**Types**: `str` vs `int`. |
| **M-06** | **The Artist**<br>*"Draw your gamer tag."* | Text is boring. We want graphics. We need to understand the X,Y grid to place pixels. | **Objects**: Creating a `Draw` object.<br>**Methods with Args**: Passing parameters.<br>**Tuples**: Grouping data like Colors (R,G,B).<br>**Coordinates**: Top-Left (0,0). |
| **B-02** | **BOSS BATTLE: The ID Card**<br>*"Digital Badge"* | **Challenge**: distinct layers (Photo, Name, Rank) combined into one image.<br>*No Guide. Pure creation.* | *Consolidating Class structure, Imports, Variables, and Drawing methods.* |

### Phase 3: The Data Harvester (Data & APIs)
*Focus: Fetching the world's information and showing it.*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-07** | **The Inspector**<br>*"Show RAM/CPU usage."* | The machine has a heartbeat. We can read it using system dictionaries. | **Dictionaries**: Key/Value pairs.<br>**Accessing Data**: `stats['cpu']`.<br>**Libraries**: Using 3rd party tools (`psutil`). |
| **M-08** | **The Forecaster**<br>*"Build a weather station."* | The world is full of data. APIs let us ask "What is the weather?" and get a JSON answer. | **APIs**: `requests.get()` (Calling a phone number).<br>**JSON**: Understanding nested data structures.<br>**Keys**: Keeping secrets (API Keys) safe. |
| **M-09** | **The Tracker**<br>*"Watch Crypto/Stocks."* | We have too much data. We need to filter lists to find just the one item we care about. | **Lists**: Ordered collections.<br>**Indexing**: `prices[0]`.<br>**Float Math**: Decimal math. |
| **B-03** | **BOSS BATTLE: The Dashboard**<br>*"3-Panel Info Cycle"* | **Challenge**: Fetch Weather AND Hardware stats, display side-by-side.<br>*Managing multiple data sources and complex layout.* | *Consolidating Dictionaries, APIs, Lists, and Layout logic.* |

### Phase 4: The Architect (Logic & Control)
*Focus: Making the system smart and autonomous.*

| ID | Title & Hook | The "Why" (Motivation) | Key Concepts Deconstructed |
| :--- | :--- | :--- | :--- |
| **M-10** | **The Night Watch**<br>*"Auto Dark Mode."* | The screen is too bright at night. The code must *decide* which colors to use based on time. | **Conditionals**: `if/else` (Making decisions).<br>**Booleans**: `True` / `False`.<br>**Comparison**: `>`, `<`, `==`. |
| **M-11** | **The Looper**<br>*"Countdown Timer."* | We need to count down from 10. Writing a print statement 10 times is stupid. Loops let us repeat. | **Loops**: `for i in range(10):`.<br>**While Loops**: `while active:`.<br>**Sleep**: `time.sleep()`. |
| **M-12** | **The Guardian**<br>*"Crash Protection."* | Sometimes the internet fails. The program should not die; it should handle the error. | **Exceptions**: `try:` / `except:` (Safety nets).<br>**Scope**: Local vs Global variables.<br>**Logging**: Proper error tracking. |
| **B-04** | **BOSS BATTLE: The Smart Frame**<br>*"Context Aware Display"* | **Challenge**: If Wifi is down -> Show Clock. If Wifi is up -> Show Weather.<br>*Complex logic trees.* | *Consolidating Control Flow, Error Handling, and State.* |
