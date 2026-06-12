# 01 — Booleans: True & False

A **boolean** is the simplest data type: it has only **two** possible values — `True` or `False`.
Every decision a program makes ("is the user logged in?", "is the cart empty?", "did the model
return text?") eventually boils down to a boolean.

| You write | Meaning |
|-----------|---------|
| `True`    | yes / on / correct |
| `False`   | no / off / incorrect |
| `type(True)` | `<class 'bool'>` |

## 🎤 Talking points (what to say & focus on)
- **This is the whole point of today.** Booleans are tiny, but `if` statements (Module 04) only
  understand `True`/`False`. Master booleans → conditionals become easy.
- **Capital T, capital F.** This is the #1 beginner error. `true`, `TRUE`, `False ` are not
  booleans. `true` gives a `NameError` because Python thinks it's a variable name.
- **`True` vs `"True"`.** Quotes change everything: `"True"` is *text* (a string), not a boolean.
  Demo `type()` on both side by side — it lands hard.
- **Booleans come from questions.** You rarely type `True` yourself; it usually pops out of a
  comparison like `age >= 18`. Foreshadow Module 02 here.
- **Secret: `True == 1`, `False == 0`.** Fun fact that explains `True + True == 2`. Don't dwell —
  just plant it so the truthiness lesson (Module 03) feels natural.
- **AI tie-in:** later, every guardrail you write ("is this prompt safe?", "did the API call
  succeed?") returns a boolean. This is the foundation of every `if` in your agent code.

## ⚠️ Common mistakes to call out
- Writing `true` / `false` (lowercase) → `NameError`.
- Wrapping in quotes by accident: `"False"` is *always* truthy (non-empty string!) — a classic bug.
- Confusing `=` (assignment) with `==` (comparison) — covered next module, but warn them now.

Run the examples:

```bash
python booleans.py
```

➡ Next: [02-comparison-operators](../02-comparison-operators/)
