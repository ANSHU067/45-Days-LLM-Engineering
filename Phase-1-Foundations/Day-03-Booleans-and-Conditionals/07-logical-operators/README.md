# 07 — Logical Operators: `and` / `or` / `not`

These glue booleans together so one condition can ask several questions at once.

| Operator | True when… | Memory hook |
|----------|------------|-------------|
| `and` | **both** sides are True | strict — everything must pass |
| `or`  | **at least one** side is True | generous — one is enough |
| `not` | flips it (`not True` → `False`) | the opposite |

### Truth tables
```
A      B      A and B    A or B
True   True   True       True
True   False  False      True
False  True   False      True
False  False  False      False
```

## 🎤 Talking points (what to say & focus on)
- **`and` = strict, `or` = generous.** That one-liner is the whole module. `and` needs *all*
  conditions; `or` needs *any* one. Use everyday framing: "18 AND has ticket" vs "weekend OR holiday."
- **`not` reads like English** — `if not logged_in:`. Encourage that phrasing; it's clean Python.
- **Precedence: `not` → `and` → `or`** (think BODMAS, but for logic). `and` binds tighter than `or`.
  Show `True or False and False` → `True`, because `and` runs first. This *will* surprise them.
- **Always reach for parentheses** when mixing `and`/`or`. Don't make readers (or yourself) memorise
  precedence — `(a or b) and c` is self-documenting. This is the single best habit from this module.
- **Build a real combo live:** the discount example `is_member and (cart_total >= 1000 or first_order)`.
  Parentheses force the `or` first — exactly the intent. Great place to pause and unpack.
- **Short-circuiting (bonus but worth it):** in `A and B`, if `A` is `False`, Python never even looks
  at `B`. In `A or B`, if `A` is `True`, `B` is skipped. The `expensive_check()` demo proves it.
  Real use: `if user and user.is_admin` — the left guards the right from crashing.
- **AI tie-in:** guardrails stack with `and`/`or` — `if response and "unsafe" not in response and len(response) < 4000:`. You'll write these constantly.

## ⚠️ Common mistakes to call out
- Using `&` / `|` (those are *bitwise* operators) instead of `and` / `or`.
- Assuming `or` means "exactly one" — it's "at least one" (inclusive or).
- Relying on precedence instead of parentheses → subtle logic bugs.
- `if x == 1 or 2:` — a classic trap. `2` is truthy, so this is *always* True. You must write
  `if x == 1 or x == 2:`.

Run the examples:

```bash
python logical_operators.py
```

➡ Next: **[exercises/](../exercises/)** — Tweet Checker, BMI Calculator & Rock-Paper-Scissors
