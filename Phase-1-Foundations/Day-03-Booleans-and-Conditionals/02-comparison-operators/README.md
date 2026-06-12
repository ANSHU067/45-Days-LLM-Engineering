# 02 — Comparison & Equality Operators

These six operators **ask a question** and hand back a boolean. They are how you *generate*
`True`/`False` from real data.

| Operator | Question | Example | Result |
|----------|----------|---------|--------|
| `>`  | greater than | `5 > 3` | `True` |
| `<`  | less than | `5 < 3` | `False` |
| `>=` | greater than or equal | `5 >= 5` | `True` |
| `<=` | less than or equal | `4 <= 3` | `False` |
| `==` | **equal to** | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |

## 🎤 Talking points (what to say & focus on)
- **`=` vs `==` is the single most important slide today.** One `=` *assigns* (puts a value into a
  box). Two `==` *asks* (is this equal to that?). Beginners mix these up constantly. Write both on
  the board: `x = 5` (do this) vs `x == 5` (ask this).
- Show that `if x = 5:` is a **SyntaxError** — Python actually protects you here, which is nice.
- **`>=` and `<=`** — the equals sign goes *second* (`>=`, never `=>`). `=>` is a syntax error.
- **Strings compare alphabetically**, not by length. `"apple" < "banana"` is `True`. Drop the
  surprise: **uppercase sorts before lowercase** (`"Zoo" < "apple"` is `True`) because it compares
  the underlying character codes (ASCII/Unicode). Mention this is why sorting can look "wrong."
- **Case sensitivity:** `"cat" == "Cat"` is `False`. Tie back to Day 2 — that's why we `.lower()`
  things before comparing user input. Foreshadow the Rock-Paper-Scissors exercise.
- **Comparing across types:** `10 == 10.0` is `True` (value match), but `10 == "10"` is `False`
  (number vs text — never equal). And `10 < "10"` is a **TypeError** — you can't *order* a number
  against a string. Equality is safe across types; ordering is not.

## ⚠️ Common mistakes to call out
- `=` where `==` was meant (assignment vs comparison).
- `=>` instead of `>=`.
- Comparing user `input()` (always a string) to a number: `input() == 5` is *always* `False`.
  You must cast: `int(input()) == 5`.

Run the examples:

```bash
python comparison_operators.py
```

➡ Next: [03-truthiness-and-in](../03-truthiness-and-in/)
