# 06 — Nesting Conditionals

A **nested** conditional is an `if` *inside* another `if`. The inner check only happens once the
outer check has passed. Each level inward = **one more indent**.

```python
if age >= 18:            # outer gate (level 1)
    if has_ticket:       # inner gate (level 2 — 8 spaces in)
        print("Welcome!")
```

## 🎤 Talking points (what to say & focus on)
- **Indentation tells the whole story.** Walk the levels out loud: 0 spaces (outer `if`), 4 spaces
  (its body), 8 spaces (inner `if`'s body). The indent is literally the nesting.
- **When to nest:** when the inner question *only makes sense* after the outer one is true. "Are you
  18? *Then* do you have a ticket?" If you're not 18, the ticket is irrelevant — so it lives inside.
- **When NOT to nest:** if you're just combining two `True/False` checks, `and` is cleaner (show the
  commented flattened version, foreshadowing Module 07). Teach the judgment, not just the mechanic.
- **Nesting gives you tailored messages per level** — "too young" vs "old enough but no ticket" vs
  "welcome." A single `and` can only say pass/fail. That's the real reason to nest.
- **Don't over-nest.** Three or four levels deep gets unreadable ("arrow code"). If it's getting
  deep, that's a smell — usually `and`/`or` or an early `else` flattens it. Plant this good habit now.
- **AI tie-in:** agent routing is nested decisions — "if logged in → if admin → show dashboard."
  The login/role example is a real shape they'll write.

## ⚠️ Common mistakes to call out
- Under-indenting the inner block so it accidentally belongs to the outer level (silent logic bug,
  not always an error).
- Mixing tabs and spaces across levels → `IndentationError`.
- Nesting when a simple `and` would read better.

Run the examples:

```bash
python nesting_conditionals.py
```

➡ Next: [07-logical-operators](../07-logical-operators/)
