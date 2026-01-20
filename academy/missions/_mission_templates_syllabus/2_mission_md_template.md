# Mission Instructions Template (Enhanced)

Use this template to create mission.md files that align with our problem-driven teaching philosophy.

---

# Mission Instructions: [Mission Name]

**Objective**: [One sentence describing WHAT you'll build]

**Estimated Time**: [X hours]

---

## Before You Start

> **Knowledge Check**: Make sure you're ready for this mission!

### You Should Already Know (from previous missions):

- ✅ [Prerequisite concept 1] (learned in [Mission ID])
  - Example: "What a class is (C-02)"
- ✅ [Prerequisite concept 2] (learned in [Mission ID])
  - Example: "What inheritance means (C-03)"
- ✅ [Prerequisite concept 3]
  - Example: "How to create a BasePlugin subclass (C-02, C-03)"

**Quick self-check**: Can you explain [key prerequisite] in one sentence? If yes, you're ready! If no, review [specific mission].

### New Concepts This Mission:

- 🆕 [New concept 1] - [One-sentence description]
  - Example: "HTTP requests - How browsers talk to servers"
- 🆕 [New concept 2] - [One-sentence description]
  - Example: "Code reading - Tracing execution flow through files"
- 🆕 [New concept 3] - [One-sentence description]

**Where to learn**: All new concepts are explained in `briefing.md`. For quick definitions, see [GLOSSARY.md](../../../_mission_templates_syllabus/GLOSSARY.md).

### Don't Worry If You Don't Know:

- ❌ [Advanced topic not required]
  - Example: "Flask/FastAPI frameworks (we'll explain what you need)"
- ❌ [Related but out-of-scope concept]
  - Example: "Networking details (not needed for this mission)"
- ❌ [Future topic]
  - Example: "Advanced web development (we only cover basics)"

**The rule**: If it's not in "You Should Already Know" or "New Concepts", you don't need it for this mission!

---

## Why This Mission Matters

[2-3 paragraphs connecting to real-world applications and stating the core problem]

**Real-world connection**: [Name specific apps, games, or tools the student uses daily that rely on these concepts. Be concrete: "Instagram's grid layout", "Fortnite's inventory system", "Your phone's settings menu"]

**The problem we're solving**: [Describe the pain/mess that happens WITHOUT these concepts. Be specific with an example showing code duplication, hard-coded values, or maintenance nightmares]

**What success looks like**: 
- **Technically**: [Tangible output - "3 boxes appear, changing one variable updates all"]
- **Conceptually**: [Deep understanding - "You'll understand WHY variables make code maintainable"]
- **Practically**: [Transfer skill - "You can apply this pattern to any layout problem"]

---

## Step 0: Understand the Problem First

**Before writing any code, build your mental model:**

1. **Read `briefing.md`** - Understand the problem story, see before/after examples, learn why these concepts exist

2. **Mental Model Check** - After reading the briefing, write your answers:
   
   **Q: In one sentence, what problem does this mission solve?**
   
   [Leave blank space for student to fill]
   
   **Q: What would break or become painful without these concepts?**
   
   [Leave blank space for student to fill]

3. **Ready check**: Can you explain the problem to someone who hasn't read the briefing? If yes, proceed. If no, re-read the "Problem Story" section.

---

## Build (Incremental Checkpoints)

Work through these checkpoints sequentially. Each one is a mini-victory!

### 🎯 CHECKPOINT 1: [First Small Win] (Estimated: X minutes)

**Goal**: [Specific, testable outcome that proves basic setup works]

**Why this checkpoint matters**: [Connection to concepts - "This proves your plugin is registered correctly"]

**Steps**:
1. [Specific command or action]
2. [Specific command or action]
3. [Test action]

**✅ Success Looks Like**:
- [ ] [Concrete thing you see - "Plugin appears in dropdown"]
- [ ] [Concrete thing you see - "No error messages in terminal"]

**🚫 If Stuck**:
- Common issue 1: [What went wrong + how to fix]
- Common issue 2: [What went wrong + how to fix]
- Debug command: `[specific command to run]`

**💭 Pause and Reflect** (30 seconds):
*[One question connecting what they just did to a concept]*
- Example: "You just created plugin-info.json. What would happen if the 'id' field didn't match the folder name?"

---

### 🎯 CHECKPOINT 2: [Second Win] (Estimated: X minutes)

**Goal**: [Next incremental outcome]

**Why this checkpoint matters**: [Connection to concepts]

**Steps**:
[...]

**✅ Success Looks Like**:
[...]

**💭 Pause and Reflect**:
*[Question that builds on previous checkpoint]*

---

### 🎯 CHECKPOINT 3: [Core Functionality] (Estimated: X minutes)

**Goal**: [The main technical win - using the core concept]

**Why this checkpoint matters**: [This is where concept X becomes concrete]

**Steps**:
1. Open `[mission_file].py`
2. Find TODO #1: [Description]
3. [Specific guidance without giving answer]

**✅ Success Looks Like**:
- [ ] [Specific visual output]
- [ ] [Specific behavior when you change a variable]

**💭 Pause and Reflect**:
*Compare and count:*
- Without [concept]: You would need ___ lines of code
- With [concept]: You need ___ lines of code
- **Key insight**: [Concept] helps by ___

---

### 🎯 CHECKPOINT 4: [Complete Feature] (Estimated: X minutes)

**Goal**: [Final polish - mission fully functional]

**Steps**:
[...]

**✅ Success Looks Like**:
[...]

---

## Practice Challenges (Learning Through Experimentation)

Inside `[mission_file].py`, you'll find TODO markers for these challenges. Each challenge has a **learning objective** - it's not just about making it work, but understanding WHY.

### 🎯 Challenge 1: [Name] 
**Learning Objective**: [Specific concept or skill]

**The Challenge**:
[Specific task description]

**Observe This**:
[What to watch for that demonstrates the concept]

**Reflection Question**:
- [Question that tests understanding of this specific challenge]

---

### 🎯 Challenge 2: Break It to Understand It
**Learning Objective**: [Understanding boundaries and failure modes]

**The Challenge**:
[Ask them to intentionally break something to see what happens]
- Example: "Set padding to 0. What breaks? Why?"

**Observe This**:
[What the broken version looks like]

**Reflection Question**:
- What does this teach you about [concept]?

---

### 🎯 Challenge 3: Adapt to Change
**Learning Objective**: [Testing flexibility and maintainability]

**The Challenge**:
[Simulate a real-world requirement change]
- Example: "Designer says: 'Make it work for 5 boxes instead of 3'"

**Count This**:
- How many lines of code did you change? ___
- How many places in the code needed updates? ___
- Would this be easier or harder without [concept]? Why?

---

## Self-Learning Module (Required)

Complete these exercises to deepen your understanding:

📝 **explain.md** - Answer line-specific questions about a [different example using same patterns]
- Tests: Can you recognize the pattern in unfamiliar code?

🐛 **debug_detective.md** - Debug broken code with [common mistakes]
- Tests: Can you spot anti-patterns and explain why they're wrong?

🔄 **bad_code.py** - Experience the 4-stage refactoring journey
- Stage 1: See working code (without [concept])
- Stage 2: Feature request → Experience the pain (count lines changed)
- Stage 3: Refactor with [concept]
- Stage 4: Same feature request → Feel the relief (count again, compare!)

📊 **bad_code_explain.md** - Analyze with concrete metrics
- Part 1: Change Impact Metrics
- Part 2: Team Collaboration Test
- Part 3: Scalability Stress Test
- Part 4: When "Bad" is Acceptable
- Part 5: Real-World Connections

**Run validation**:
```bash
cd ~/InkyPi/academy/missions/[mission_folder]
python3 check.py
```

This validates your work and helps you identify gaps.

---

## Success Criteria (Skills You've Proven)

Run `python3 check.py`, but understand what success MEANS:

### ✅ Skill 1: [Concept A] - [Practical Application]

**The Test**:
- [ ] [Specific action - e.g., "Change variable X"]
- [ ] [Observable result - e.g., "All 3 boxes move"]
- [ ] [Code efficiency - e.g., "Only 1 line of code changed"]

**This Proves**: [Connection to concept - e.g., "One variable controls multiple elements (DRY principle)"]

**Metrics** (from bad_code exercise):
- Without [concept]: ___ lines changed
- With [concept]: ___ lines changed
- Improvement ratio: ___ : 1

---

### ✅ Skill 2: [Concept B] - [Practical Application]

**The Test**:
- [ ] [Specific action]
- [ ] [Observable result]

**This Proves**: [Connection to concept]

**Real-World Parallel**: [Example from apps they use - "Just like how Instagram adapts to different screen sizes"]

---

### ✅ Skill 3: Pattern Recognition (from explain.md)

**The Test**:
- [ ] Answered questions about [different example] correctly
- [ ] Identified line-specific roles (classes vs objects, etc.)
- [ ] Designed a new system using same patterns

**This Proves**: You can RECOGNIZE and APPLY these patterns in new situations, not just memorize definitions

---

### ✅ Skill 4: Debugging & Maintenance (from debug_detective.md)

**The Test**:
- [ ] Found all [N] bugs in the broken code
- [ ] Connected each bug to a concept from the briefing
- [ ] Fixed the code using proper patterns

**This Proves**: You understand not just "what works" but "what's wrong and why"

---

## 🎯 Overall Success = Understanding, Not Just Functionality

**You've truly succeeded when you can**:
- [ ] Explain the problem this mission solves (to someone who hasn't coded)
- [ ] Predict what breaks when you change code
- [ ] Justify design decisions with metrics (X:Y improvement ratio)
- [ ] Transfer the pattern to a completely different domain

**"It works" is baseline. "I understand WHY and WHEN" is success.**

---

## Quick Reference Commands

**Create plugin folder**:
```bash
mkdir -p src/plugins/[mission_id]
```

**Copy template**:
```bash
cp academy/missions/[mission_folder]/[mission_file].py src/plugins/[mission_id]/
```

**Restart service**:
```bash
sudo systemctl restart inkypi.service
```

**Validate mission**:
```bash
cd ~/InkyPi/academy/missions/[mission_folder]
python3 check.py
```

**Test bad_code exercise**:
```bash
cd ~/InkyPi/academy/missions/[mission_folder]
python3 bad_code.py
```

**View service logs** (if debugging):
```bash
sudo journalctl -u inkypi.service -f
```

---

## Workflow Reminder

**Development flow** (MacBook → GitHub → Raspberry Pi):
1. Edit code in VS Code on MacBook
2. Commit and push to GitHub
3. SSH into Raspberry Pi
4. `git fetch && git checkout [your-branch]`
5. Restart service and test

**When stuck**:
1. Read the error message completely
2. Check which checkpoint you're at
3. Review that checkpoint's "If Stuck" section
4. Re-read relevant section in briefing.md
5. Ask for help (after trying the above)

---

## Mission-Specific Notes

[Add any special notes, gotchas, or tips specific to this mission]

---

## Completion Checklist

Before moving to the next mission:

- [ ] All checkpoints completed (plugin works)
- [ ] All practice challenges attempted
- [ ] Self-learning module filled out (explain.md, debug_detective.md, bad_code.py, bad_code_explain.md)
- [ ] `check.py` passes
- [ ] Can explain the problem and solution to someone else
- [ ] Understand when to use/not use these concepts
- [ ] Filled all "Pause and Reflect" questions in this document

**Time to celebrate!** You've not just built a plugin, you've mastered a thinking pattern.

---

## After This Mission

**Concepts you've internalized**:
- [List key concepts from this mission]

**Next mission preview**: [One sentence about what's next and why it builds on this]

**How to review later**: Re-run the bad_code.py exercise in 2 weeks. If you can still explain the improvement ratio, you've truly learned it.
