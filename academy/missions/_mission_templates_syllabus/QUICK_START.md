# QUICK START: Creating a New Mission

**Use this guide when AI is asked to generate a new mission.**

---

## Step-by-Step Process

### 1. Get Mission Details from syllabus.md

**AI Prompt**:
```
Look at syllabus.md and find mission [ID] (e.g., C-04).
Tell me:
- Mission name
- Core concepts
- Learning objectives
- Prerequisites
```

**Example Output**:
- ID: C-04
- Name: List Practice
- Concepts: Lists, Indexing, Iteration,  append()
- Objective: Manage multiple items without separate variables
- Prerequisite: C-01 (Variables), C-02 (Classes)

---

### 2. Create briefing.md

**Use Template**: `1_briefing_template.md`

**AI Prompt**:
```
Create briefing.md for mission C-04 (List Practice).
Follow the exact structure from 1_briefing_template.md.

Core concepts: Lists, Indexing, Iteration

Include:
1. Problem: Managing 10 high scores with 10 separate variables (score1, score2...)
2. Pain: Adding 11th score = create new variable + update all display code
3. Solution: One list with 10 items
4. Benefits: Add score = one line (scores.append()), not 10 lines of variable creation
5. Real-world: Leaderboards, shopping carts, playlists
6. Before/after for each concept (lists, indexing, iteration)
7. Metrics: 30 lines (10 variables) → 5 lines (1 list), 6:1 improvement
```

**Validation**: Check that briefing includes:
- [ ] Problem story with concrete pain (10 variables)
- [ ] Solution with list at solving it
- [ ] 2-3 real-world examples (leaderboards, shopping)
- [ ] Before/after for each concept
- [ ] Metrics (line counts, ratios)
- [ ] Scalability context (10 items → 100 items)

---

### 3. Create mission.md

**Use Template**: `2_mission_md_template.md`

**AI Prompt**:
```
Create mission.md for C-04.
Follow 2_mission_md_template.md structure exactly.

Include:
1. Why This Mission Matters (leaderboards, shopping carts)
2. Mental Model Check (write: what problem do lists solve?)
3. 4 Incremental Checkpoints:
   - CHECKPOINT 1 (5 min): Plugin registers
   - CHECKPOINT 2 (10 min): Create empty list
   - CHECKPOINT 3 (15 min): Add items with append()
   - CHECKPOINT 4 (20 min): Display all items with loop
4. Practice Challenges:
   - Challenge 1: Add/remove items (count operations)
   - Challenge 2: Break it (access index 100, observe error)
   - Challenge 3: Different data (names instead of scores)
5. Skills-Based Success (5 skills with metrics)
```

**Validation**: Check that mission includes:
- [ ] Why This Mission Matters section
- [ ] Mental Model Check with blank spaces
- [ ] 4 checkpoints with time estimates
- [ ] Reflection prompts after each checkpoint
- [ ] Practice challenges with learning objectives
- [ ] Skills-based success criteria (not just "it works")

---

### 4. Create Self-Learning Exercises

**Use Template**: `3_self_learning_template.md`

**AI Prompt**:
```
Create all self-learning files for C-04 using 3_self_learning_template.md.

explain.md:
- Use DIFFERENT example: shopping cart items (not high scores)
- 22 line-specific questions about shopping cart code
- Transfer challenge: Design a todo list system

debug_detective.md:
- Broken code with 3 list-related bugs:
  * Accessing wrong index
  * Forgetting to append()
  * Using wrong loop variable
- Debug steps: predict, locate, diagnose, fix, explain

bad_code.py:
- Stage 1: 10 separate score variables (working code)
- Stage 2: Feature request - "Add 11th score + 12th score" (experience pain)
- Stage 3: Refactor with list
- Stage 4: Same feature request (feel relief)

bad_code_explain.md:
- Part 1: Metrics (Stage 2 vs 4 line counts)
- Part 2: Team ("teammate adds 13th score")
- Part 3: Scalability (100 scores scenario)
- Part 4: When lists are overkill (1-2 items)
- Part 5: Real-world (Spotify playlists)
```

**Validation**: Check that files include:
- [ ] explain.md uses different example (shopping, not scores)
- [ ] debug_detective.md has 3 concept-specific bugs
- [ ] bad_code.py has all 4 stages marked
- [ ] bad_code_explain.md has 5 parts with metrics

---

### 5. Create check.py

**Use Template**: `4_check_py_template.md`

**AI Prompt**:
```
Create check.py for C-04 using 4_check_py_template.md.

Customize:
- plugin_id = "c04_list_practice"
- Mission name = "List Practice"
- explain.md keywords: ["shopping", "cart", "items", "todo", "task"]
- debug_detective.md keywords: ["index", "append", "bug"]
- mission_concept = "lists and iteration"
- 5 skills for completion feedback:
  * Lists prevent variable sprawl (10:1 ratio)
  * Indexing accesses specific items
  * Iteration processes all items
  * append() grows lists dynamically
  * Knowing when NOT to use lists (Rule of Three)
```

**Validation**: Check that check.py includes:
- [ ] Correct plugin_id
- [ ] Keywords match the different example (shopping, not scores)
- [ ] 5 mission-specific skills in completion feedback
- [ ] Helpful hints for each file type

---

### 6. Create Code Template

**AI Prompt**:
```
Create c04_list_practice.py template file.

Include:
- Checkpoint markers (# CHECKPOINT 1, 2, 3, 4)
- Detailed comments explaining list concepts
- Progressive TODOs aligned with mission.md checkpoints
- Learning notes section at bottom (when to use lists, metrics, examples)
- FakeDraw preview capability for testing

Structure:
1. Imports
2. CHECKPOINT 2: Create empty list
3. CHECKPOINT 3: Add items with append()
4. CHECKPOINT 4: Display with loop
5. Practice TODOs
6. Plugin class with generate_image()
7. Learning notes section
```

**Validation**: Check that template includes:
- [ ] Checkpoint comments matching mission.md
- [ ] TODOs for each checkpoint
- [ ] Detailed docstrings
- [ ] Learning notes (metrics, when to use, examples)

---

## File Checklist

After generation, verify all files exist:

**Mission Files**:
- [ ] `briefing.md` - Problem-driven narrative
- [ ] `mission.md` - Incremental checkpoints
- [ ] `{mission_id}.py` - Code template with TODOs
- [ ] `check.py` - Validation script

**Self-Learning Files**:
- [ ] `explain.md` - Different example with 22 questions
- [ ] `debug_detective.md` - 3 bugs to find and fix
- [ ] `bad_code.py` - 4-stage refactoring
- [ ] `bad_code_explain.md` - 5-part metrics analysis

---

## Quality Checks

### briefing.md
- [ ] Shows concrete pain (line counts, specific scenarios)
- [ ] Before/after code for each concept
- [ ] 2-3 real-world examples students know
- [ ] Metrics throughout (ratios, percentages)
- [ ] Team/scalability perspective

### mission.md
- [ ] "Why This Mission Matters" with real apps
- [ ] Mental Model Check with writing prompts
- [ ] 4 checkpoints with time estimates
- [ ] Reflection after each checkpoint
- [ ] Skills-based success (not "it works")

### Self-Learning
- [ ] explain.md uses DIFFERENT example
- [ ] 22 questions (not generic, very specific)
- [ ] debug_detective.md has concept-specific bugs
- [ ] bad_code.py has 4 stages clearly marked
- [ ] bad_code_explain.md has metrics (improvement ratios)

### check.py
- [ ] Validates structure (4 stages, 5 parts)
- [ ] Keywords match different example
- [ ] 5 mission-specific skills
- [ ] Helpful hints for failures

---

## Common Mistakes to Avoid

❌ **Don't**:
- Use mission code as explain.md example (must be different!)
- Create generic bugs in debug_detective (make them concept-specific)
- Skip metrics in bad_code_explain.md (need line counts!)
- Make checkpoints too big (keep each 5-20 min)
- Write generic success criteria ("it works")

✅ **Do**:
- Use different example in explain.md (shopping vs scores)
- Create bugs that teach the concept (index errors for lists)
- Include concrete metrics (10 variables → 1 list = 10:1)
- Break work into small victories (checkpoints)
- Celebrate specific skills with metrics

---

## Time Estimate

Creating a complete mission with AI assistance:
- briefing.md: 10-15 minutes
- mission.md: 15-20 minutes
- Self-learning files: 20-25 minutes
- check.py: 10 minutes
- Code template: 15-20 minutes

**Total**: ~70-90 minutes for a complete mission

---

## Reference Examples

**Best reference**: Mission C-03 Inheritance Practice
- `/academy/missions/c03_inheritance_practice/`
- Shows all templates fully implemented
- Problem-driven briefing
- Incremental mission structure
- Complete self-learning exercises
- Enhanced check.py

**Study this mission** to see what "done right" looks like!
