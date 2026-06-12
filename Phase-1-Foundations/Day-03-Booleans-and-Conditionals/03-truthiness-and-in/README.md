# 03 — Truthiness, Falsiness & the `in` Operator

Python lets you use **any** value where a boolean is expected. In that moment, every value counts as
either **truthy** (acts like `True`) or **falsy** (acts like `False`).

### The falsy values (memorise this short list)
| Value | Why it's falsy |
|-------|----------------|
| `False` | it literally is |
| `0` / `0.0` | zero |
| `""` | empty string |
| `None` | the "nothing" value (from Day 2) |
| `[]` `{}` `()` | empty collections (Day 6 preview) |

**Everything else is truthy** — any non-zero number, any non-empty string (yes, even `"0"` and a
single space `" "`).

## 🎤 Talking points (what to say & focus on)
- **Use `bool(x)` as an x-ray.** It shows you exactly how a value will behave inside an `if`. Run it
  on a bunch of values live.
- **The killer gotcha:** `bool("0")` is **`True`** and `bool(" ")` is **`True`**. Students assume
  `"0"` is falsy because `0` is — but it's a *non-empty string*. This causes real bugs.
- **Why it's useful:** instead of `if len(name) > 0:` you can write `if name:`. Cleaner, idiomatic
  Python. Show the empty-input demo — press Enter with nothing and watch the else branch fire.
- **`None` is falsy** — connect back to Day 2's "special value None." Functions that return nothing
  return `None`, and `if result:` neatly catches that.
- **The `in` operator** returns a boolean: "is the left thing *inside* the right thing?" For strings
  it's a substring check. `"AI" in "I love AI"` → `True`. Still **case-sensitive**.
- **`not in`** reads like English and is the clean opposite — prefer it over `not (x in y)`.
- **AI tie-in:** `if "error" in response.lower():` is exactly how you'll sanity-check model output
  later. This operator shows up constantly in LLM glue code.

## ⚠️ Common mistakes to call out
- Thinking `"0"`, `"False"`, or `" "` are falsy — they are **truthy** (non-empty strings).
- Forgetting `in` is case-sensitive (`"ai" in "AI tools"` is `False`).
- Using `in` on a number — `5 in 555` is a **TypeError**; `in` needs a string/collection on the right.

Run the examples (it asks for input):

```bash
python truthiness_and_in.py
```

➡ Next: [04-if-elif-else](../04-if-elif-else/)
