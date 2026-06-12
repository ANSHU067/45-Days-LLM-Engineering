# 04 — Conditionals: `if` / `elif` / `else`

This is the payoff for booleans. A conditional **runs a block of code only when a condition is
`True`.** It's how a program makes decisions.

```python
if condition:        # note the colon :
    do_this()        # indented = "inside" the if (runs only if True)
do_this_always()     # not indented = always runs
```

| Keyword | When it runs |
|---------|--------------|
| `if`   | when its condition is `True` |
| `elif` | "else if" — checked only if the ones above were `False` |
| `else` | catch-all — runs if **nothing** above matched |

## 🎤 Talking points (what to say & focus on)
- **The colon `:` and the indentation are not optional — they ARE the syntax.** Python has no
  `{ }` braces. The indented block *is* the body of the `if`. Forgetting the colon or the indent is
  the most common error today.
- **Standard indent = 4 spaces.** Be consistent. **Never mix tabs and spaces** — Python throws
  `TabError`/`IndentationError`. Tell them: let the editor insert spaces (VS Code does by default).
- **`if` alone** = "do this *only if*." Show that the un-indented line after it always runs — drives
  home what "inside the block" means.
- **`if/else`** = exactly one of two paths *always* runs.
- **`elif` chain**: Python checks **top to bottom and stops at the first `True`.** This is the
  single most important concept of the module. Use the grade example: 72 hits `>= 60` and **stops** —
  it never reaches the lower checks.
- **Order matters!** If you put the loosest condition (`>= 40`) first, everything above 40 grabs it.
  Always order from strictest to loosest (or most-specific to least). Demo the bug by reordering.
- **A block can hold many lines** — all the lines at the same indent run together (the Premium
  customer example).
- **AI tie-in:** every agent is a giant `if/elif/else` over what the user asked or what the model
  returned. "If the response contains a tool call, run the tool; elif it's an answer, show it; else
  ask again." This pattern never leaves you.

## ⚠️ Common mistakes to call out
- Missing `:` after the condition.
- No indentation (or wrong/mixed indentation) → `IndentationError` / `TabError`.
- Using `=` instead of `==` in the condition.
- Wrong branch order so a loose condition "eats" the specific ones.

Run the examples:

```bash
python if_elif_else.py
```

➡ Next: [05-random-numbers](../05-random-numbers/)
