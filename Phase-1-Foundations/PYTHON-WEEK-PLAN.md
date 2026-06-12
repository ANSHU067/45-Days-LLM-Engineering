# 🐍 Python Power-Up Week — Detailed Plan (Days 1–7)

The prerequisite week of **SSAI-101**. Goal: take students with *only* Python basics and lock in
every skill the LLM track (Day 8+) assumes. Source outline: [`../dump/python.txt`](../dump/python.txt);
day ranges fixed by [`../COURSE-PLAN.md`](../COURSE-PLAN.md).

> **Audience:** complete beginners (pre-final/final-year B.Tech, BCA/MCA). One concept per module,
> heavily-commented runnable `.py`, India-context examples, free-tier only.

## Status at a glance
| Day | Topic | Build status |
|----:|-------|--------------|
| 1 | Setup, data types, operators & variables | ✅ Built & verified |
| 2 | Strings, f-strings & string methods | ✅ Built & verified (+ trainer's guide) |
| 3 | Booleans, conditionals & logic | 📋 Planned (folder has career talk only) |
| 4 | Loops | 📋 Planned |
| 5 | Functions & scope | 📋 Planned |
| 6 | Data structures | 📋 Planned |
| 7 | Errors, modules & OOP | 📋 Planned |

## Per-day shape (every day is identical in structure)
Each day = a `Day-NN-Topic/` folder following the repo convention:
`README.md` (objectives + module table + how-to-run + exercise) · numbered `NN-concept/` modules
(teaching `README.md` + runnable `snake_case.py`) · `exercises/` (stub `# TODO` + `_solution.py`) ·
`career-talk/` (the 30-min deck) · optionally `TRAINERS-GUIDE.md`.

**Standard 3.5-hour session timing** (per [`../COURSE-PLAN.md`](../COURSE-PLAN.md)):

| Block | Time | Use |
|-------|:----:|-----|
| Career talk | 30 min | The day's `career-talk/` deck |
| Concept + live coding | 75 min | Trainer-led walk through the modules (REPL-first) |
| Guided code-along | 45 min | Students type along; TA floats |
| Independent work | 45 min | The day's exercises |
| Standup + wrap | 15 min | Recap + preview next day |

## The dependency chain (why this order)
`variables/types (D1)` → `strings (D2)` → `booleans→conditionals (D3)` → `loops (D4)` →
`functions/scope (D5)` → `data structures (D6)` → `errors/modules/OOP (D7)` → **ready for the AI track (D8)**.
Each day only forward-references the next minimally (e.g. f-strings appeared D2 before functions; flag and move on).

---

## ✅ Day 1 — Setup, Data Types, Operators & Variables
*Built. 8 modules + 3 exercises + opening Software-Engineering presentation.*

| # | Module | Covers |
|--:|--------|--------|
| 00 | presentation-software-engineering-basics | Big-picture map (frontend/backend/API/DB/Git/cloud/AI) |
| 01 | running-python | REPL vs script files; first program |
| 02 | numbers | int, float, numeric notations |
| 03 | operators | arithmetic + `//`, `%`, `**` |
| 04 | comments | single/inline/block |
| 05 | variables | storing values, reassignment, dynamic typing |
| 06 | variable-naming | rules, conventions, keywords |
| 07 | assignment-operators | `+=`, `-=`, `*=`, … |
| 08 | print-function | `sep`, `end`, multiple values |

**Exercises:** Magic Trick · Seconds-in-a-day · Split the Bill.

---

## ✅ Day 2 — Strings, f-strings & String Methods
*Built. 8 modules + 3 exercises + trainer's guide.*

| # | Module | Covers |
|--:|--------|--------|
| 01 | strings | quotes, `+` concat, `*` repeat |
| 02 | string-indexing | indexing, negative, immutability, `None` |
| 03 | string-slices | `[start:stop:step]`, `[::-1]` |
| 04 | escape-and-triple-quotes | `\n \t \" \\`, multi-line (→ LLM prompts) |
| 05 | len-input-typecasting | `len()`, `input()`, `int()/float()/str()` |
| 06 | f-strings | embedded expr, `:.2f` / `:,` / `:.0%` |
| 07 | string-methods | upper/lower/title/strip/replace/find, `help()` |
| 08 | method-chaining | back-to-back calls, `split`/`join` taster |

**Exercises:** Age Calculator · Shopping Cart · Press Release.

---

## 📋 Day 3 — Booleans, Conditionals & Logic
**Folder:** `Day-03-Booleans-and-Conditionals` · **Objective:** make programs *decide*.

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | booleans | `True`/`False`, `bool` type | Introducing Booleans |
| 02 | comparison-operators | `< > <= >= == !=`, comparing across types | Comparison/Equality Operators |
| 03 | truthiness-and-in | truthy/falsey values, the `in` operator | Truthiness & Falseyness, "in" Operator |
| 04 | if-elif-else | conditionals + indentation rules | If/Elif/Else keywords, Indentation |
| 05 | nesting-conditionals | conditionals inside conditionals | Nesting Conditionals |
| 06 | logical-operators | `and` / `or` / `not` + precedence | Logical AND/OR/NOT, Precedence |
| 07 | random-numbers | `random.randint()` (for the games) | Generating Random Numbers |

**Exercises:** `tweet_checker` (length check, booleans) · `bmi_calculator` (if/elif/else) ·
`rock_paper_scissors` (logic + random) — RPS is the headline.
**Learning checks:** explain truthiness of `0`/`""`/`[]`; trace an `and`/`or` precedence expression.
**Gotchas to stage:** `=` vs `==`; indentation errors; `if x = 5` SyntaxError.

---

## 📋 Day 4 — Loops
**Folder:** `Day-04-Loops` · **Objective:** repeat work without repeating code.

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | while-loops | `while`, conditions, **avoiding infinite loops** | While Loops, Avoiding Infinite Loops |
| 02 | for-loops | iterating sequences (strings, soon lists) | For Loops, Loops & Indentation |
| 03 | range | `range(stop/start,stop/step)` | The range() function |
| 04 | break-and-continue | early exit + skip | Break and Continue |
| 05 | nested-loops | loops inside loops (grids, patterns) | Working With Nested Loops |

**Exercises:** `number_guessing_game` (while + input + random — ties D3 in) · `bottles_of_beer`
(for + range, the classic countdown) · `dice_roller` (loops + random).
**Stretch:** `toothpick_game` (2-player logic refactor).
**Gotchas to stage:** off-by-one in `range`; the infinite `while True` without `break`; forgetting to
update the loop variable.

---

## 📋 Day 5 — Functions & Scope
**Folder:** `Day-05-Functions-and-Scope` · **Objective:** package logic into reusable, named blocks.

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | defining-functions | `def`, calling, why functions | Introducing/First Function |
| 02 | parameters-and-arguments | one & multiple inputs | Functions With Input(s) |
| 03 | return-values | `return` vs `print`; using results | Introducing/Using Return |
| 04 | default-and-keyword-args | defaults, ordering, named args | Default Params, Keyword Arguments |
| 05 | scope-legb | local/enclosing/global/built-in + `global` | Global/Local/Enclosing Scope, Precedence |
| 06 | args-and-kwargs | `*args`, `**kwargs`, unpacking, mutable-default gotcha | *args, **kwargs, Mutable Default Args |

**Exercises:** `calculator_functions` (params + return) · `greeter` (default/keyword args) ·
`sum_all` (`*args`).
**Learning checks:** difference between `return` and `print`; predict a LEGB scope puzzle.
**Gotchas to stage:** function that prints but returns `None`; the mutable default arg `def f(x=[])`.

---

## 📋 Day 6 — Data Structures
**Folder:** `Day-06-Data-Structures` · **Objective:** store and organise collections of data.
*(Densest pre-OOP day — budget time carefully; lists get two modules.)*

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | lists-basics | create, index, update, mutability | Creating/Accessing/Updating Lists |
| 02 | list-methods | append/extend/insert/pop/remove/sort/reverse/count | List Methods, Sort/Reverse/Count |
| 03 | list-slicing-and-loops | slices, iteration, list+loop patterns | List Slices, Iterating, Patterns |
| 04 | nested-lists-and-copying | nested lists, `==` vs `is`, copy, `split`/`join`, unpacking | Nested Lists, Copying, Join/Split, Unpacking |
| 05 | dictionaries | create, `get`/`in`, add/update, `pop`/`del`, iterate keys/values/items, merge | Dictionaries (all) |
| 06 | tuples | immutability, why/when to use | Tuples |
| 07 | sets | uniqueness, union/intersection/difference, when to use | Sets |

**Exercises:** `grand_prix` (lists + loops) · `todo_list` (list CRUD via menu) ·
`peak_dictionary` (dict iteration + lists-in-dicts).
**Gotchas to stage:** list aliasing (`b = a` shares the same list) vs `a.copy()`; `KeyError` vs `.get()`;
mutating a list while iterating.

---

## 📋 Day 7 — Errors, Modules & OOP
**Folder:** `Day-07-Errors-Modules-and-OOP` · **Objective:** handle failure, reuse code, model with classes.
*(The most packed day — three sub-topics. See prioritisation note below.)*

| # | Module | Covers | `python.txt` source |
|--:|--------|--------|---------------------|
| 01 | error-types | common exceptions; reading tracebacks | Common Error Types |
| 02 | try-except | handling, `raise`, LBYL vs EAFP | Try/Except, Raising, LBYL/EAFP |
| 03 | modules-and-imports | built-in modules, import syntax, custom modules | Built-In Modules, Import Syntax, Custom Modules |
| 04 | pip-and-pypi | 3rd-party packages, `pip install` | Pip & PyPI, First Pip Package |
| 05 | classes-and-objects | `class`, instances, `__init__`, instance methods | Class Syntax, Instance Methods |
| 06 | class-attributes-and-methods | class attributes, class methods | Class Attributes/Methods |
| 07 | inheritance-and-super | inheritance, `super()` | Inheritance Basics, super() |

**Exercises:** `custom_module` (write + import your own `.py`) · `bank_account` (a class with methods) ·
`sentiment_analysis` (install a pip package — the fun mini-project bridging into the AI track).
**Prioritisation (if short on time):** Errors (01–02) and OOP (05–07) are load-bearing for the AI
track; `pip` (04) is essential for Day 8+. Custom-module depth (03) can compress.
**Gotchas to stage:** bare `except:` swallowing everything; `self` forgotten in methods; mutable
class attributes shared across instances.

---

## What students can do after Day 7 (entry check for Day 8)
- [ ] Read input, branch with `if/elif/else`, and loop with `for`/`while`.
- [ ] Write functions with parameters, defaults, and return values.
- [ ] Use lists & dicts fluently (the shape of all JSON / API data).
- [ ] `try/except` around risky code; `pip install` a package and import it.
- [ ] Read and write a basic class (needed for Pydantic models on Day 8/11).

## Production checklist (when building each planned day)
1. Read the day's row above + the matching `python.txt` lessons.
2. Create modules in order; one concept each; runnable `.py` + teaching `README.md`.
3. Add `exercises/` (stub `# TODO` + `_solution.py`).
4. **Run every script** with the real CPython (`…\Python312\python.exe`) before marking done.
   ⚠️ Avoid printing `₹` (Windows console can't encode it — use `Rs`; see Day 2 Module 06).
5. Update this file's status table + the phase/root READMEs + CLAUDE.md status.
6. Career deck already exists in each `career-talk/`; add a `TRAINERS-GUIDE.md` if desired.
