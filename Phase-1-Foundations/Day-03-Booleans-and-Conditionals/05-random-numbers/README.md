# 05 — Random Numbers with `random`

`random` lets your program produce unpredictable values — perfect for games, simulations, and
quick demos. It ships with Python (standard library), so there's nothing to install.

```python
import random
random.randint(1, 6)   # a whole number from 1 to 6 (BOTH ends included)
```

| Function | What it does | Example |
|----------|--------------|---------|
| `random.randint(a, b)` | random integer, `a` and `b` **both included** | `randint(1, 6)` → `1..6` |
| `random.choice(seq)` | pick one item at random | `choice(["a","b"])` |
| `random.seed(n)` | make randomness reproducible | `seed(42)` |

## 🎤 Talking points (what to say & focus on)
- **`import random` is their first taste of a module.** Keep it light — "Python ships with batteries;
  `import` plugs one in. Full lesson on Day 7." Don't rabbit-hole.
- **`randint(a, b)` is INCLUSIVE on both ends.** `randint(1, 6)` *can* return 6. This trips people up
  — many languages exclude the top. Say it explicitly.
- **Re-run the file a few times** so they *see* the number change. That "aha, it's different each
  time" moment is the lesson.
- **This is why we learned conditionals first** — random value *in*, decision *out*. Coin flip and
  the lucky-number game show the combo. This is the heart of the **Tweet Checker** and
  **Rock-Paper-Scissors** exercises.
- **`random.choice`** is the cleanest way to pick from options — preview it; RPS will use it.
- **`random.seed(n)`** (optional/advanced): same seed → same sequence. Useful for testing and for
  making a demo behave identically every time. Mention it's how ML experiments stay reproducible.
- **Honesty note:** this is *pseudo*-random (good enough for games, **not** for passwords/crypto —
  use the `secrets` module for that). One sentence is plenty.

## ⚠️ Common mistakes to call out
- Forgetting `import random` → `NameError`.
- Assuming `randint(1, 6)` stops at 5 (it includes 6).
- Comparing a random int to `input()` without `int()` — string vs number never matches.

Run the examples (it asks for a guess):

```bash
python random_numbers.py
```

➡ Next: [06-nesting-conditionals](../06-nesting-conditionals/)
