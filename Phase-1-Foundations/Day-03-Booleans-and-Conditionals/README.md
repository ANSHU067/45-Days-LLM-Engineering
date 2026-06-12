# Day 03 — Booleans, Conditionals & Logical Operators

Days 1–2 gave you data (numbers and text). Today your programs learn to **make decisions**. Every
`if` you'll ever write — and every branch inside an AI agent — rests on one tiny data type: the
**boolean** (`True`/`False`). We build from a single boolean up to full multi-condition logic.

> 🎤 **Trainer?** Follow the minute-by-minute [`TRAINERS-GUIDE.md`](TRAINERS-GUIDE.md) — full session
> script (career talk → modules → exercises → wrap-up) with live-coding cues, the exact gotchas to
> stress, and timings.

## Learning objectives
By the end of today you can:
- Use **booleans** (`True`/`False`) and explain `True == 1`, `False == 0`
- Generate booleans with **comparison/equality operators** (`> < >= <= == !=`) and avoid the `=` vs `==` trap
- Predict **truthy vs falsy** values and use the **`in`** membership operator
- Branch with **`if` / `elif` / `else`** — and understand why **indentation is the syntax**
- Produce randomness with **`random.randint` / `random.choice`**
- **Nest** conditionals and know when to flatten them instead
- Combine conditions with **`and` / `or` / `not`**, respecting **precedence** (and using parentheses)

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [booleans](01-booleans/) | `True`/`False`, `bool` type, `"True"` vs `True`, `True == 1` |
| 02 | [comparison-operators](02-comparison-operators/) | `> < >= <= == !=`, the `=` vs `==` trap, comparing across types |
| 03 | [truthiness-and-in](03-truthiness-and-in/) | Truthy/falsy values, `bool()`, `in` / `not in` |
| 04 | [if-elif-else](04-if-elif-else/) | Conditionals, branch order, indentation as syntax |
| 05 | [random-numbers](05-random-numbers/) | `import random`, `randint` (inclusive!), `choice`, `seed` |
| 06 | [nesting-conditionals](06-nesting-conditionals/) | `if` inside `if`; when to nest vs use `and` |
| 07 | [logical-operators](07-logical-operators/) | `and` / `or` / `not`, truth tables, precedence, short-circuit |

Then test yourself in **[exercises/](exercises/)**.

## The 5 things to really nail today
1. **`=` assigns, `==` asks.** The #1 source of bugs all week.
2. **Capital `True`/`False`** — and `"True"` (quotes) is a string, not a boolean.
3. **Falsy list:** `0`, `0.0`, `""`, `None`, empty collections. Everything else (even `"0"`) is truthy.
4. **Indentation is the syntax** — 4 spaces, never mix tabs/spaces; `elif` stops at the first `True`.
5. **`and` = all, `or` = any, `not` = flip** — and use **parentheses** when you mix them.

## How to run
From this folder, run any file directly:

```bash
python 01-booleans/booleans.py
```

Several files (Modules 03, 05 and the exercises) use `input()` — they'll **pause and wait** for you
to type and press Enter. That's expected.

Or open the REPL and experiment:

```bash
python
>>> 5 >= 3 and "AI" in "I love AI"
True
```

## Today's exercises
Three of them — see [`exercises/`](exercises/):
1. **Tweet Checker** — truthiness + `if/elif/else` length validation
2. **BMI Calculator** — `float()` casting + an `if/elif/elif/else` chain
3. **Rock, Paper, Scissors** — `random`, `in`, and combining `and`/`or`

➡ Next: **Day 04 — Loops** *(coming soon)*
