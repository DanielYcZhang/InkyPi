# Template: How to Write briefing.md

Use this template to create the `briefing.md` file for any mission.

---

## Structure Overview

Every briefing.md should follow this exact structure:

1. **Title & Introduction** (1 paragraph)
2. **The Problem: [Pain Without Concepts]** (3-4 paragraphs with code)
3. **The Solution: [Concepts to the Rescue]** (2-3 paragraphs with code)
4. **Breaking It Down** (One section per concept)
5. **Key Principle** (Summary)
6. **What "Success" Looks Like** (Outcomes)

---

## 1. Title & Introduction

```markdown
# Briefing: [Mission ID] — [Mission Name]

[One paragraph describing what students will build and what core concept they'll learn]

Example:
"You will build a base card and then a special card that **inherits** from it. 
This mission teaches why inheritance exists and when to use `super()`."
```

---

## 2. The Problem: [Show the Pain]

**Purpose**: Make students FEEL the pain of not using the concept

**Structure**:
```markdown
## The Problem: [Catchy Title]

Imagine you're building [real scenario]. You need [task that requires concept].

Without [concept], your code looks like this:

```python
# Show messy code with duplications/problems
[Bad code example - 15-20 lines]
```

**The Pain Points:**
- **Lines X-Y** are copy-pasted in all N classes (Z duplicated lines!)
- Your designer says: "[change request]" → You need to change N places
- You add a Nth item → Copy-paste the shared code AGAIN
- You forget to update one → [specific bug example]

**When [designer/manager] makes M changes, you're changing N places. One missed update = broken [app/game].**
```

**Tips**:
- Use concrete numbers (3 classes, 9 duplicated lines)
- Show real change scenarios ("Make border thicker")
- Calculate the pain (3 places → 30 places with 10 items)

---

## 3. The Solution: [Concepts to the Rescue]

**Purpose**: Introduce concepts as the hero that solves the mess

**Structure**:
```markdown
## The Solution: [Concept Name] to the Rescue

**[Concept]** is like [powerful analogy]. [Explain analogy in 2-3 sentences]

Think of it like [Manufacturing example]:
- **Base Class** = [platform/foundation that all share]
- **Subclasses** = [specialized versions that inherit + add unique parts]

Each [subclass] **inherits** the [shared parts], then adds its specialty. 
If [base] improves [shared feature], ALL [subclasses] get it automatically!

Here's the same [task] with [concept]:

```python
# Show clean code using concepts
[Good code example - should be significantly shorter]
```

**Benefits:**
- [Shared code] written ONCE (in [BaseClass])
- Designer says "[same change request]"? → Change ONE place
- Add M more types? → Each only writes N lines (their unique part)
- Shared behavior stays consistent across ALL [items]
- No copy-paste = no bugs from forgetting to update one

**When [designer] makes M changes to shared elements, you change 1 place instead of N.**
```

**Tips**:
- Strong analogy (Car manufacturing, building blueprints)
- Side-by-side comparison with Problem section
- Quantify benefits (1 change vs 30 changes)

---

## 4. Breaking It Down

**Purpose**: Detailed explanation of each concept with before/after

**Structure** (Repeat for each concept):

```markdown
## Breaking It Down

### 1) [Concept Name] = "[One-Liner Description]"

**Analogy**: Like [relatable metaphor]. [Expand in 1-2 sentences]

**Definition**: [Technical but clear explanation in 1-2 sentences]

**Before/After:**

```python
# Before (no [concept]): [Show the pain]
[Code showing the problem - 8-12 lines]

# After (with [concept]): [Show the solution]
[Code showing the fix - 4-6 lines]
```

**Why Better**: [Explain the improvement with numbers]. 
Before = edit N classes. After = edit 1 class.

**Common Mistakes**:
- [Mistake 1]: [What it is + how to fix]
- [Mistake 2]: [What it is + how to fix]

**Where Used**: [Specific line range] in `[mission_file].py`

**Scalability Context**: 
With N items, before = X duplicated lines. After = Y lines (Z% reduction!).
When M people work on this, [explain how concept helps collaboration].
```

**Tips**:
- Each concept gets its own subsection
- Always include before/after code
- Quantify the improvement
- Connect to where it's used in mission
- Add scalability perspective

---

## 5. Key Principle

```markdown
## Key Principle: [DRY / Encapsulation / Abstraction / etc.]

[Concept] is the answer to: "[The specific problem it solves]"

**Rule of Thumb**:
- N-M items with similar code? → [When to use concept]
- M+ items with similar code? → Time to [apply concept]
- Changing shared code requires updating N places? → DEFINITELY need [concept]
```

---

## 6. What "Success" Looks Like

```markdown
## What "Success" Looks Like

- [Technical outcome 1]: [Specific code behavior]
- [Technical outcome 2]: [Specific code structure]
- [Understanding outcome]: Changing [base] affects all [subclasses] (intentionally!)
- [Maintainability outcome]: Code is shorter, clearer, and easier to maintain

Use/avoid guidance is practiced in `bad_code.py`.
```

---

## Mission-Specific Customization

### For Different Concept Types:

**Variables/Loops** (C-01):
- Problem: Hard-coded values everywhere
- Pain: Change padding? Update 12 places
- Solution: Variables + loops
- Analogy: Recipe with ingredients (variables)

**Classes** (C-02):
- Problem: Scattered variables (name1, name2, name3...)
- Pain: Add property? Update 10 places per creature
- Solution: Class as blueprint
- Analogy: Car blueprint → specific cars

**Inheritance** (C-03):
- Problem: Duplicated code across similar classes
- Pain: Change shared code? Update 5 classes
- Solution: Base class + inheritance
- Analogy: Toyota platform → Camry/RAV4/Prius

**Functions** (C-04):
- Problem: Copy-pasted calculation blocks
- Pain: Fix bug? Find all 8 copy-paste locations
- Solution: DRY with functions
- Analogy: Kitchen recipe you can reuse

---

## Real-World Connection Examples

Always include 2-3 apps/games students know:

**For Classes/Objects**:
- Pokemon: 1000+ creatures, each is an object
- Contact app: Each contact is an object
- Fortnite inventory: Each item is an object

**For Inheritance**:
- Hearthstone cards: Base card + specialized types
- Mobile RPG: Base character → Warrior/Mage/Rogue
- Pokemon TCG: All cards have HP → Each type adds unique

**For Lists**:
- Leaderboards: High scores list
- Shopping cart: Items list
- Spotify: Playlist is a list

**For Loops**:
- Instagram grid: Loop through photos
- Game inventory: Loop through items
- Settings menu: Loop through options

---

## Checklist: Is My Briefing Complete?

- [ ] Title with mission ID and name
- [ ] Introduction (1 paragraph, what + why)
- [ ] Problem section showing messy code
- [ ] Pain points with concrete numbers
- [ ] Solution section with clean code
- [ ] Benefits with metrics (1 change vs 30)
- [ ] Breaking It Down: Each concept

 has:
  - [ ] Analogy
  - [ ] Definition
  - [ ] Before/After code
  - [ ] Why Better (with numbers)
  - [ ] Common Mistakes
  - [ ] Where Used in mission
  - [ ] Scalability Context
- [ ] Key Principle (rule of thumb)
- [ ] What Success Looks Like
- [ ] 2-3 Real-world examples students know
- [ ] Team/collaboration perspective
- [ ] Metrics throughout (line counts, ratios)

---

## Example Reference

See `/academy/missions/c03_inheritance_practice/briefing.md` for a complete example following this template.

**Key features to emulate**:
- Problem shows 3 card classes with duplicated 9 lines each
- Solution shows BaseCard + inheritance reducing to 9 total lines
- Each concept has before/after comparison
- Scalability: "With 20 card types, 600 lines → 100 lines"
- Team: "Designer changes border → 1 update vs 20 updates"
- Real-world: Hearthstone, Pokemon TCG, mobile RPGs

---

## Common Pitfalls to Avoid

❌ **Don't**:
- Start with definitions (boring!)
- Show only syntax (not WHY)
- Use abstract examples (not relatable)
- Skip the pain section (students won't appreciate solution)
- Forget metrics (make improvements concrete)
- Omit real-world examples

✅ **Do**:
- Start with the problem/pain
- Show concrete code (before/after)
- Use apps students know
- Quantify improvements (3:1 ratio, 50% reduction)
- Include team/scalability thinking
- Make it a story (problem → solution → success)
