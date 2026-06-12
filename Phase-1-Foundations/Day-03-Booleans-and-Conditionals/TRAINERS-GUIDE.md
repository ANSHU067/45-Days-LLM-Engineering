# 🎤 Trainer's Guide — Day 03: Booleans, Conditionals & Logical Operators

A minute-by-minute script you can follow live. Covers the full session: the 30-min **career talk**,
the technical modules (with exactly what to *say*, what to *type*, what to *ask*, and the *gotchas*
to pre-empt), the independent exercises, and the wrap-up.

> **Audience reminder:** complete beginners (Day 3). They know numbers (Day 1) and strings (Day 2).
> Today is the day code starts to *think* — sell that: "your programs stop just calculating and start
> **deciding**." Everything builds toward the `if` inside every AI agent.

---

## 0. Before the session (5-min pre-flight)
- [ ] Projector mirrored; font size **large** (terminal + editor at ≥18pt).
- [ ] A terminal open in the Day-03 folder; `python` REPL ready to launch.
- [ ] Editor open on `Phase-1-Foundations/Day-03-Booleans-and-Conditionals/`.
- [ ] Run one script once to confirm Python works: `python 01-booleans/booleans.py`.
- [ ] Use the **real CPython**: `C:\Users\PC\AppData\Local\Programs\Python\Python312\python.exe`.
- [ ] Open the career deck `career-talk/index.html` in a browser, press **F** (fullscreen), clicker paired.
- [ ] ⚠️ Modules 03, 05 and all exercises use `input()` — they **pause**. Decide if you'll type live or
      pipe answers (e.g. `printf "rock\n" | python ...`).

## Session map (3 hrs 30 min)

| Block | Time | What |
|-------|:----:|------|
| Career talk | 30 min | Deck: today's Career Launchpad topic |
| Concept + live coding | 75 min | Modules 01–04 (booleans → if/elif/else) |
| Guided code-along | 45 min | Modules 05–07 (random, nesting, and/or/not) |
| Independent work | 45 min | The 3 exercises |
| Standup + wrap-up | 15 min | Recap, blockers, preview Day 4 |

*Running behind? See the **Triage** box at the very end for what to cut safely.*

---

## 1. Career talk — 30 min
Deck: [`career-talk/index.html`](career-talk/) · notes in [`career-talk/README.md`](career-talk/README.md).

- Present the slides (~28 min) and collect today's **Career Action** ask aloud.
- **Bridge into code (1 line):** *"A job application is a decision: do you match the role, yes or no?
  Programs make decisions the exact same way — with booleans and `if`. Today we learn to make code
  decide."*

---

## 2. Concept + live coding — 75 min (Modules 01–04)
Teach from the REPL where you can. **Type live, make a mistake on purpose, let them predict outputs.**

### 🔥 Cold open (2 min)
In the REPL, ask "True or False?" *before* hitting Enter:
```python
>>> 10 > 3
>>> "AI" in "I love AI"
>>> bool("0")          # <- the surprise: True!
```
The `bool("0")` result gets a reaction — promise "you'll know exactly why in 20 minutes."

### Module 01 — Booleans (10 min) · `01-booleans/`
- **One message:** there are only two values, `True` and `False`, and they power every decision.
- **⚠️ Gotcha #1 (stage it):** type `true` → `NameError`. "Capital T, capital F. Always."
- **⚠️ Gotcha #2:** `type(True)` vs `type("True")` — boolean vs string. Quotes change everything.
- **Plant the seed:** `True + True` → `2`. "Secretly True is 1, False is 0. Hold that thought."
- **Check:** "Is `"False"` (in quotes) a boolean?" → No, it's a string (and it's *truthy*!).

### Module 02 — Comparison & equality (12 min) · `02-comparison-operators/`
- **THE slide of the day:** `=` assigns, `==` asks. Write both: `x = 5` (do) vs `x == 5` (ask).
- **Stage the bug:** `if x = 5:` → `SyntaxError`. "Python protects you here — be grateful."
- **Type live:** `5 == 5`, `5 != 3`, `"apple" < "banana"`, then `"Zoo" < "apple"` → `True` (surprise:
  uppercase sorts first). `"cat" == "Cat"` → `False` (callback to Day 2 `.lower()`).
- **Across types:** `10 == 10.0` (True), `10 == "10"` (False), `10 < "10"` → `TypeError`.
- **Check:** "Why is `int(input()) == 5` needed instead of `input() == 5`?" → input is a string.

### Module 03 — Truthiness & `in` (13 min) · `03-truthiness-and-in/`
- **Pay off the cold open.** `bool()` is an x-ray. Run it on `0, "", None, "0", " ", -5`.
- **🔑 The killer point:** the falsy list is short — `0, 0.0, "", None, []`. **Everything else is
  truthy**, including `"0"` and `" "`. Write the falsy list on the board.
- **Why it's useful:** `if name:` instead of `if len(name) > 0:`. Run the empty-input demo — press
  Enter with nothing, watch the `else` fire.
- **`in`:** "is the left inside the right?" → returns a boolean. `"AI" in "I love AI"` → True.
  Still case-sensitive. Show `not in` reads like English.
- **Check:** "Is `bool(" ")` True or False?" → True (a space is non-empty).

### Module 04 — if / elif / else (20 min) · `04-if-elif-else/`  ⭐ *the headline skill of the day*
- **The colon and the indent ARE the syntax.** No `{ }` in Python. Forget either → error.
- **Type live, build up:** `if` alone → `if/else` → full `if/elif/else` grade example.
- **🔑 The core idea:** Python checks **top to bottom and stops at the first `True`.** Prove it with
  the grade example — 72 hits `>= 60` and never checks lower.
- **⚠️ Order matters:** reorder so `>= 40` comes first and watch 72 wrongly become "D". Unforgettable.
- **Indentation tangent:** 4 spaces, consistent. **Never mix tabs/spaces** → `TabError`. Let the
  editor handle it. Show a multi-line block (all same-indent lines run together).
- **Check:** "If I put `marks >= 40` first, what grade does 95 get?" → "D" — order bug.

---

## 3. Guided code-along — 45 min (Modules 05–07)
Slow down. **Everyone types with you.** TA floats to unstick people.

### Module 05 — Random numbers (12 min) · `05-random-numbers/`
- `import random` — "their first module. Python ships with batteries; full lesson Day 7."
- **⚠️ `randint(1, 6)` includes BOTH 1 and 6.** Many languages exclude the top — Python doesn't.
- **Re-run the file 3×** so they SEE the number change. That's the lesson.
- Combine with conditionals: coin flip + lucky-number game. Preview `random.choice` (RPS uses it).
- **Honesty note (1 line):** pseudo-random — fine for games, not passwords (`secrets` for that).
- **Check:** "Can `randint(1, 6)` ever give 6?" → Yes.

### Module 06 — Nesting conditionals (13 min) · `06-nesting-conditionals/`
- **Indentation tells the story:** 0 → 4 → 8 spaces = outer → body → inner. Walk it out loud.
- **When to nest:** when the inner question only matters *after* the outer passes ("18? then ticket?").
- **When NOT to:** show the commented flattened `and` version. "Don't over-nest — arrow code is a smell."
- **Why nest at all:** tailored messages per level ("too young" vs "no ticket" vs "welcome").
- **Check:** "Should `age >= 18` and `has_ticket` always be nested?" → No, `and` is cleaner if you
  only need pass/fail.

### Module 07 — Logical operators (20 min) · `07-logical-operators/`
- **One-liner:** `and` = all, `or` = any (at least one), `not` = flip. Walk the truth tables.
- **`not` reads like English:** `if not logged_in:`. Encourage it.
- **⚠️ Precedence:** `not` → `and` → `or`. Type `True or False and False` → `True` (and runs first).
  **"Always use parentheses when you mix them."** Best habit of the day.
- **Build live:** the discount combo `is_member and (cart_total >= 1000 or first_order)`.
- **⚠️ Classic trap:** `if x == 1 or 2:` is *always* True (2 is truthy). Must write `x == 1 or x == 2`.
- **Short-circuit (bonus):** `False and expensive()` never runs `expensive()`. Show the demo.
- **Check:** "Rewrite `if day == "Sat" or day == "Sun"` — is `or day == "Sun"` needed, or can I write
  `or "Sun"`?" → needed; `or "Sun"` is always truthy.

---

## 4. Independent work — 45 min (Exercises)
Point them to [`exercises/`](exercises/). Stubs have `# TODO`s; solutions are `*_solution.py`.
**Try the stub first**, peek only when stuck. Suggested order = easiest first.

| Order | Exercise | Skills | Watch for |
|------:|----------|--------|-----------|
| 1 | `tweet_checker.py` | truthiness, `if/elif/else`, `len` | catch the **empty** case first |
| 2 | `bmi_calculator.py` | `float()`, `**`, elif chain | using `int()` not `float()` for height |
| 3 | `rock_paper_scissors.py` | `random`, `in`, `and`/`or` | not `.lower()`-ing input; combo logic |

**Live-verify a solution** to model good habits (pipe answers since they use `input()`):
```bash
printf "Learning AI is fun\n" | python exercises/tweet_checker_solution.py
printf "68\n1.75\n" | python exercises/bmi_calculator_solution.py
printf "rock\n" | python exercises/rock_paper_scissors_solution.py
```
**Stretch for fast finishers:** Tweet Checker "getting close" warning over 260 chars; BMI reject
non-positive numbers; RPS keep score (peek at Day 4 loops).

---

## 5. Standup + wrap-up — 15 min
- **Go around (1 line each):** "one thing that clicked, one thing still fuzzy." Note repeat fuzzies.
- **Recap the 3 keepers of the day:**
  1. **`=` assigns, `==` asks.** And capital `True`/`False`.
  2. **`if/elif/else` stops at the first match** — order your branches strict → loose; indentation is syntax.
  3. **`and` = all, `or` = any, `not` = flip** — parenthesise when you mix them.
- **Career nudge:** remind them to do today's Career Action from the deck.
- **Preview Day 4:** "Loops — doing something *many* times without copy-paste. Today's `if` runs once;
  tomorrow `while`/`for` run it again and again. RPS becomes best-of-5."

---

## ❓ Anticipated student questions (quick answers)
- *"Why two equals signs?"* One `=` puts a value in a box; two `==` asks if two things are equal.
- *"Is `"0"` true or false?"* Truthy — it's a non-empty string. Only `0` (the number) is falsy.
- *"Difference between `and` and `&`?"* Use `and`/`or` for logic; `&`/`|` are bitwise (different thing).
- *"Can I have many `elif`s?"* Yes, as many as you like. Only the first True one runs.
- *"Tabs or spaces?"* Spaces (4). Never mix — Python errors. Let the editor insert them.
- *"Does `randint(1,6)` include 6?"* Yes — both ends included.
- *"Why did `10 < "10"` crash but `10 == "10"` didn't?"* Equality across types is allowed (just False);
  *ordering* a number against a string is a TypeError.

## 🧯 Triage — if you're running behind
Cut in this order (lowest learning-loss first):
1. Skip the short-circuit demo in Module 07 and all stretch goals.
2. Make `rock_paper_scissors.py` a take-home instead of in-class.
3. Compress Module 06 (nesting) to the one concert example — `and` flattening as a one-liner.
4. Trim Module 05's `seed()` and the honesty note.
5. **Never cut:** `==` vs `=` (02), `if/elif/else` order (04), and `and`/`or` precedence+parentheses
   (07) — they're load-bearing for every program from here on.

## 🎯 Success check (leave the room able to…)
- [ ] Explain the difference between `=` and `==`, and write a correct comparison.
- [ ] List the falsy values and predict `bool("0")`.
- [ ] Write an `if/elif/else` chain with branches in the correct order.
- [ ] Combine two conditions with `and`/`or` and parenthesise correctly.
- [ ] Use `random.randint`/`choice` inside a conditional (the RPS pattern).
