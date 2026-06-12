# Day 03 — Exercises

Put today's tools to work: booleans, comparisons, truthiness, `if/elif/else`, `random`, and
`and/or/not`. Try each in the stub file first, then check the matching `*_solution.py`.

---

## Exercise 1 — Tweet Checker 🐦
A tweet can be **1–280 characters**. Tell the user whether theirs is postable.

**Your task:** in `tweet_checker.py`
1. `input()` the tweet and measure it with `len()`.
2. **Empty first:** an empty string is *falsy* — catch `if not tweet:` before anything else.
3. `elif` length ≤ 280 → "✅ Good to post! (N/280 chars)".
4. `else` → tell them how many characters **over** they are (`length - 280`).

*Skills:* `len()`, truthiness, `if/elif/else`, f-strings.
*Focus:* ordering branches correctly (empty → ok → too long).

➡ Solution: [`tweet_checker_solution.py`](tweet_checker_solution.py)

---

## Exercise 2 — BMI Calculator 🩺
Compute Body Mass Index and classify it. `BMI = weight(kg) / height(m)²`.

| BMI | Category |
|-----|----------|
| `< 18.5` | Underweight |
| `18.5 – 24.9` | Normal |
| `25 – 29.9` | Overweight |
| `≥ 30` | Obese |

**Your task:** in `bmi_calculator.py`
1. `input()` weight and height — **cast with `float()`** (height is a decimal like `1.75`).
2. Compute `bmi = weight / (height ** 2)`.
3. Use an `if/elif/elif/else` chain (lowest → highest) for the category.
4. Print the BMI to 1 decimal: `f"{bmi:.1f}"`.

*Skills:* `float()`, `**`, `if/elif/else` ordering, f-string formatting.
*Focus:* why the elif chain lets you write `bmi < 25` without repeating `bmi >= 18.5`.

➡ Solution: [`bmi_calculator_solution.py`](bmi_calculator_solution.py)

---

## Exercise 3 — Rock, Paper, Scissors ✊✋✌️
Play against the computer. Rock beats scissors, scissors beats paper, paper beats rock.

**Your task:** in `rock_paper_scissors.py`
1. `input()` the player's move; `.strip().lower()` it (Day 2!) so `"Rock"` matches `"rock"`.
2. **Validate:** if the move is `not in ["rock","paper","scissors"]`, reject it.
3. Computer plays with `random.choice(...)`. Print both moves.
4. Decide with `if/elif/else`: draw → the three player-win combos (use `and`/`or`) → else computer.

*Skills:* `random.choice`, `in`/`not in`, `and`/`or`, string methods, conditionals.
*Focus:* combining `and` (within one combo) and `or` (across the three winning combos).

➡ Solution: [`rock_paper_scissors_solution.py`](rock_paper_scissors_solution.py)

---

### Stretch goals (if you finish early)
- **Tweet Checker:** warn (don't reject) when a tweet is over **260** chars ("getting close!").
- **BMI:** reject non-positive numbers with a friendly message before calculating.
- **RPS:** loop it for best-of-3 (peek ahead to Day 4 loops) or keep score.
