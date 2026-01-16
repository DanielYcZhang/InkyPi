# Mission Templates & Syllabus - Organization Guide

This folder contains all the templates and guidelines for creating InkyPi Academy missions.

---

## 📁 Folder Structure

```
_mission_templates_syllabus/
├── README.md                          ← You are here
│
├── 📘 CURRICULUM DESIGN
│   ├── syllabus.md                   ← Overall curriculum structure
│   └── rubric.md                     ← Grading criteria
│
├── 🎯 PRIMARY TEMPLATES (Use these to create new missions!)
│   ├── 1_briefing_template.md        ← How to write briefing.md
│   ├── 2_mission_md_template.md      ← How to write mission.md  
│   ├── 3_self_learning_template.md   ← How to create self-learning exercises
│   └── 4_check_py_template.md        ← How to write check.py
│
└── 📖 PHILOSOPHY & GUIDES (Read for context, don't use as templates)
    ├── TEACHING_PHILOSOPHY.md        ← Why we structured things this way
    ├── bad_code_guide.md             ← Deep dive: Progressive refactoring
    └── example_c02/                  ← Complete example mission
        ├── briefing_example.md
        ├── mission_example.md
        └── explain_example.md
```

---

## 🚀 Quick Start: Creating a New Mission

### Step 1: Read the Curriculum
1. Open `syllabus.md` to find your mission in the curriculum
2. Note the mission ID (e.g., C-04) and core concepts

### Step 2: Use the Templates in Order
Follow these templates in sequence:

1. **`1_briefing_template.md`**
   - Creates `briefing.md` for your mission
   - Problem-driven narrative with before/after examples
   - Use the template structure exactly

2. **`2_mission_md_template.md`**
   - Creates `mission.md` for your mission  
   - Incremental checkpoints with reflection
   - Skills-based success criteria

3. **`3_self_learning_template.md`**
   - Creates `explain.md`, `debug_detective.md`, `bad_code.py`, `bad_code_explain.md`
   - Progressive refactoring exercises
   - Pattern recognition challenges

4. **`4_check_py_template.md`**
   - Creates `check.py` for your mission
   - Validates structure and depth
   - Provides helpful feedback

### Step 3: Create the Code Template
Create `{mission_id}.py` with:
- Checkpoint markers (aligning with mission.md)
- Detailed comments explaining concepts
- Progressive TODOs
- Learning notes section

---

## 📚 What Each File Does

### CURRICULUM DESIGN (Reference Only)

#### `syllabus.md`
- **Purpose**: Overall curriculum structure, learning goals, mission progression
- **Use when**: Planning the curriculum, understanding learning path
- **Don't use as**: Template for individual missions

#### `rubric.md`
- **Purpose**: How missions are graded
- **Use when**: Understanding success criteria
- **Don't use as**: Mission template

---

### PRIMARY TEMPLATES (Use These!)

#### `1_briefing_template.md`
**What it creates**: The `briefing.md` file for a mission

**Structure**:
1. Problem Story (show the pain without concepts)
2. Solution Introduction (concepts as the rescue)
3. Breaking It Down (each concept with before/after)
4. Scalability Context

**Key Features**:
- Problem-driven narrative
- Before/after code comparisons
- Real-world examples (Pokemon, Hearthstone, etc.)
- Team/scalability perspective

**Example**: See C-03's briefing.md

---

#### `2_mission_md_template.md`
**What it creates**: The `mission.md` file for a mission

**Structure**:
1. Why This Mission Matters
2. Mental Model Check
3. Incremental Checkpoints (4-6 checkpoints)
4. Practice Challenges with learning objectives
5. Skills-Based Success Criteria

**Key Features**:
- "Why this matters" section (real-world anchors)
- Reflection prompts after each checkpoint
- "Break it to understand it" challenges
- Skills proven, not just "it works"

**Example**: See C-03's mission.md

---

#### `3_self_learning_template.md`
**What it creates**: All self-learning exercise files

**Files Generated**:
- `explain.md` - New example with line-specific questions
- `debug_detective.md` - Find and fix bugs
- `bad_code.py` - 4-stage progressive refactoring
- `bad_code_explain.md` - 5-part metrics analysis

**Key Features**:
- Pattern recognition (different example)
- Metrics tracking (improvement ratios)
- Team collaboration scenarios
- Transfer challenges

**Example**: See C-03's self-learning files

---

#### `4_check_py_template.md`
**What it creates**: The `check.py` validation script

**Structure**:
1. Plugin file checks
2. Self-learning file validation (structure + depth)
3. Skills-based completion feedback
4. Helpful error hints

**Key Features**:
- Validates structure (4 stages, 5 parts, etc.)
- Checks for depth (character counts, keywords)
- Celebrates skills proven
- Guides fixes with specific hints

**Example**: See C-03's check.py

---

### PHILOSOPHY & GUIDES (Context, Not Templates)

#### `TEACHING_PHILOSOPHY.md`
- **What it is**: Explanation of our pedagogical approach
- **Read it to**: Understand WHY we structure missions this way
- **Content**: Problem-driven learning, metrics, team thinking, transfer

#### `bad_code_guide.md`
- **What it is**: Deep dive into the progressive refactoring exercise
- **Read it to**: Understand the 4-stage bad_code.py structure
- **Content**: Why we moved from "fix this" to "experience pain then relief"

#### `example_c02/` folder
- **What it is**: Complete worked example of C-02 mission files
- **Use it to**: See what a finished mission looks like
- **Content**: briefing, mission.md, explain.md examples

---

## 🎯 Mission Creation Workflow

When AI is asked to create a new mission:

### 1. **Identify Mission Details**
From `syllabus.md`:
- Mission ID (e.g., C-04)
- Core concepts (e.g., "Lists", "Iteration")
- Learning objectives
- Prerequisites

### 2. **Create briefing.md**
**Use**: `1_briefing_template.md`

**Prompt AI**:
```
Create briefing.md for mission C-04 teaching Lists and Iteration.
Use the structure from 1_briefing_template.md.

Include:
- Problem story showing messy code without lists
- Solution showing how lists solve it
- Before/after for each concept
- Real-world examples (apps students use)
```

### 3. **Create mission.md**
**Use**: `2_mission_md_template.md`

**Prompt AI**:
```
Create mission.md for C-04.
Use the structure from 2_mission_md_template.md.

Include:
- Why this matters (real apps that use lists)
- 4 incremental checkpoints
- Reflection after each checkpoint
- Practice challenges with metrics
- Skills-based success criteria
```

### 4. **Create Self-Learning Exercises**
**Use**: `3_self_learning_template.md`

**Prompt AI**:
```
Create self-learning exercises for C-04.
Use 3_self_learning_template.md.

Create:
- explain.md with different example (not the mission code)
- debug_detective.md with list-related bugs
- bad_code.py with 4-stage refactoring (list vs scattered variables)
- bad_code_explain.md with 5-part metrics analysis
```

### 5. **Create check.py**
**Use**: `4_check_py_template.md`

**Prompt AI**:
```
Create check.py for C-04.
Use 4_check_py_template.md.

Include:
- Validation for all self-learning files
- Check for structure (4 stages, etc.)
- Skills-based completion feedback (5 skills specific to C-04)
- Helpful error hints
```

### 6. **Create Code Template**
**Prompt AI**:
```
Create c04_list_practice.py template.

Include:
- Checkpoint markers (matching mission.md)
- Detailed docstrings
- Progressive TODOs
- Learning notes section (key concepts, metrics, when to use)
```

---

## 🔍 Quick Reference: Which File to Use

| **You want to create...** | **Use this template...** | **Primary/Reference** |
|----------------------------|-------------------------|----------------------|
| briefing.md | `1_briefing_template.md` | **PRIMARY** |
| mission.md | `2_mission_md_template.md` | **PRIMARY** |
| explain.md, debug_detective.md, bad_code exercises | `3_self_learning_template.md` | **PRIMARY** |
| check.py | `4_check_py_template.md` | **PRIMARY** |
| Understanding philosophy | `TEACHING_PHILOSOPHY.md` | Reference |
| Understanding bad_code approach | `bad_code_guide.md` | Reference |
| Seeing a complete example | `example_c02/` | Reference |
| Understanding overall curriculum | `syllabus.md` | Reference |
| Understanding grading | `rubric.md` | Reference |

---

## 🎨 Example: Creating Mission C-04

**Mission**: List Practice (core concepts: Lists, Indexing, Iteration)

**Step 1**: Read syllabus.md → Find C-04 details

**Step 2**: Create briefing.md
- Use `1_briefing_template.md`
- Problem: Managing 10 high scores with 10 separate variables
- Solution: One list with 10 items
- Before/after showing list vs variables
- Real-world: Leaderboards, inventory systems

**Step 3**: Create mission.md
- Use `2_mission_md_template.md`
- Checkpoint 1: Plugin registers
- Checkpoint 2: Create empty list
- Checkpoint 3: Add items to list with append()
- Checkpoint 4: Display all items with loop
- Challenge: Break it (access index 100, observe error)

**Step 4**: Create self-learning
- Use `3_self_learning_template.md`
- explain.md: Use different example (shopping cart, not high scores)
- debug_detective.md: Fix index errors, missing append()
- bad_code.py: 10 variables → list refactoring
- bad_code_explain.md: Count changes (30 lines → 5 lines)

**Step 5**: Create check.py
- Use `4_check_py_template.md`
- Check for "shopping cart" in explain.md (not "high scores")
- Validate 4 stages in bad_code.py
- Skills: Lists prevent duplication, indexing, iteration, etc.

---

## 📝 Notes for AI Mission Generators

When asked to create a new mission:

1. **Start with syllabus.md** - Get mission ID and concepts
2. **Use numbered templates (1-4)** in order
3. **Don't use summary/enhancement docs** as templates
4. **Reference C-03** as a complete example
5. **Follow the structure exactly** - don't improvise
6. **Include all sections** from templates
7. **Generate mission-specific content** - different examples, not copy-paste

---

## 🔄 Maintenance & Updates

**This folder is organized as**:
- **4 primary templates** (numbered 1-4) - USE THESE
- **2 curriculum docs** (syllabus, rubric) - REFERENCE
- **2 philosophy docs** (teaching, bad_code guide) - UNDERSTAND WHY
- **1 example folder** (C-02) - SEE IT IN ACTION

**Keep it simple**: When creating missions, only use files starting with numbers (1-4).

---

## ✅ Checklist: Have I Used the Right Template?

Before generating mission content, confirm:

- [ ] I've read the mission requirements from `syllabus.md`
- [ ] I'm using `1_briefing_template.md` for briefing.md
- [ ] I'm using `2_mission_md_template.md` for mission.md
- [ ] I'm using `3_self_learning_template.md` for all self-learning exercises
- [ ] I'm using `4_check_py_template.md` for check.py
- [ ] I understand the philosophy from `TEACHING_PHILOSOPHY.md`
- [ ] I've looked at C-03 as a reference example

**If all checked, you're ready to generate mission content!**
