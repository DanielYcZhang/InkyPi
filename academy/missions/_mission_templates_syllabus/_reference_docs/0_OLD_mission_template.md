# InkyPi Academy — Mission Template (Python)

Use this template to create new mission folders under `academy/missions/` and new learning missions in `academy/syllabus.md`.

---

## 0) Metadata
- **Mission ID**: `M-XX`
- **Codename**: `The ______`
- **Hook**: `"__________"`
- **Recommended duration**: `45–90 minutes`
- **Prereqs**: (which missions must be completed first)
- **Creates / modifies**:
  - Plugin path: `src/plugins/mXX_name/`
  - Files: list exact files the learner will touch

---

## 1) Outcome (Visible Result)
Describe what will be visible in the web UI and/or on the display.

Example:
- “A new plugin appears in the web UI with an icon, and it renders a ‘Hello Name’ card.”

---

## 2) Concepts You Will Learn (List Only)
List the concepts (no explanations here). Example:
- Variables
- Loops
- Function parameters
- Coordinates

---

## 3) Glossary (with Examples)
Define 5–10 terms with a one-line definition and a short example.
Each term should point to a real line in the mission code.

---

## 4) Briefing (Concept Explanations)
The detailed teaching happens in `briefing.md`, not in `mission.md`.

**New Structure (Problem → Solution → Deep Dive):**

### Part 1: The Problem Story
Paint a picture of messy code WITHOUT the concept:
- Show actual bad code example
- Point out the pain: "What if you need 10 creatures? 50? Copy-paste 50 times?"
- Highlight maintenance nightmare: "If you change one creature property, you need to update 50 places"

### Part 2: The Solution (Big Idea)
Introduce the concept as the hero that solves this mess:
- Use powerful analogies (Car/Toyota for classes, Factory for constructors)
- Show the same task WITH the concept
- Highlight the dramatic improvement

### Part 3: Breaking It Down (Detailed Concepts)
For each concept:
1) **Analogy**: Concrete, relatable metaphor
2) **Definition**: Technical but clear explanation
3) **Before/After Code Example** ← CRITICAL
   - Left: The painful way without it
   - Right: The elegant way with it
   - Caption: Why the right is better
4) **Common Mistakes**: Real errors learners make
5) **Where Used**: Point to exact lines in this mission
6) **Scalability Context**: "When multiple people work on this...", "When you have 100 items..."

**Key Principle**: Every concept needs a side-by-side comparison showing the pain of NOT using it.

---

## 5) Build (Smallest Slice That Works)
Write the fewest steps that produce the outcome.

**Minimum plugin skeleton**
- `plugin-info.json` with `id`, `display_name`, `class`
- Python file with a class that inherits `BasePlugin`
- A `generate_image(self, settings, device_config)` method returning a `PIL.Image`

**Stop point**: define exactly when the learner should pause and test.

---

## 6) Practice (Inside the .py Template)
All practice and “Do-It” tasks live in the `.py` template as TODOs.
Keep tasks short, visible, and safe.
Include the **Surprise** as a TODO in the `.py` template.

Include one **Bad vs Good** exercise:
- Provide `bad_code.py` and `bad_code_explain.md`.
- Ask the learner to fix the bad code and explain why it is better.
- Ask when the bad version might still be acceptable.

---

## 7) Check (Acceptance Criteria)
Write objective “done” checks:
- The plugin appears in the UI
- The plugin renders an image without crashing
- The output matches expected behavior

If you add a mission `check.py`, list exactly what it validates.

---

## 7.1) Self-Learning Module (Required)
Include the self-learning module in each mission:
- Add `explain.md` with NEW example code and line-specific questions
- Add `debug_detective.md` with broken code to fix (replaces `predict.md` and `trace.md`)
- Add `bad_code.py` and `bad_code_explain.md` for refactoring practice
- Generate `copilot_input.txt` in `check.py` for AI grading
- Extend `check.py` to validate that the files exist and are filled

**Key Changes:**
- `explain.md`: Uses a DIFFERENT example with same patterns, tests pattern recognition
- `debug_detective.md`: Debugging challenge that teaches error-reading skills
- Removed `trace.md`: Disconnected from core concepts, replaced by debugging

Template: `academy/self_learning_module.md`

---

## 8) Surprise (The Wow Moment)
Add a small surprise element (font, visual effect, data reveal).

---

## 9) Stretch (Optional)
Only if motivation is high:
- Add settings UI (`settings.html`)
- Add better layout
- Add caching/error screens
- Add a second data source

---

## 10) Reflection (1–3 Questions)
Examples:
- What part was confusing at first, and what made it click?
- What does this function return, and why?
- What would you refactor if you had 30 more minutes?
