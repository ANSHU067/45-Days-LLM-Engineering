# Day 02 — Strings, f-strings & String Methods

Yesterday you handled numbers. Today is all about **text** — the data type you'll use most when
working with LLMs (every prompt and every model reply is a string). You'll learn to build strings,
pull pieces out of them, format them cleanly with **f-strings**, and clean them up with
**string methods**.

> 🎤 **Trainer?** Follow the minute-by-minute [`TRAINERS-GUIDE.md`](TRAINERS-GUIDE.md) — full session
> script (career talk → modules → exercises → wrap-up) with live-coding cues, gotchas, and timings.

## Learning objectives
By the end of today you can:
- Create strings with single, double, and triple quotes
- Combine strings with `+` and repeat them with `*`
- Pull out characters and ranges using **indexing** and **slicing**
- Use **escape characters** (`\n`, `\t`, `\"`) and multi-line strings
- Measure with `len()`, read user input with `input()`, and convert types with `int()`/`float()`/`str()`
- Format output beautifully with **f-strings** (including `:.2f` and `:,`)
- Clean and transform text with **string methods** (`.strip()`, `.replace()`, `.title()` …) and **method chaining**

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [strings](01-strings/) | Quotes, string variables, concatenation `+`, repetition `*` |
| 02 | [string-indexing](02-string-indexing/) | Indexing, negative indexing, immutability, `None` |
| 03 | [string-slices](03-string-slices/) | `[start:stop:step]`, reversing with `[::-1]` |
| 04 | [escape-and-triple-quotes](04-escape-and-triple-quotes/) | `\n` `\t` `\"` `\\` and multi-line triple-quoted strings |
| 05 | [len-input-typecasting](05-len-input-typecasting/) | `len()`, `input()`, casting with `int()`/`float()`/`str()` |
| 06 | [f-strings](06-f-strings/) | f-strings, embedded expressions, number formatting |
| 07 | [string-methods](07-string-methods/) | `.upper/.lower/.strip/.replace/.title/.find`, `help()` & the docs |
| 08 | [method-chaining](08-method-chaining/) | Calling methods back-to-back; `.split()`/`.join()` taster |

Then test yourself in **[exercises/](exercises/)**.

## How to run
From this folder, run any file directly:

```bash
python 01-strings/strings.py
```

Some files (Module 05 and a couple of exercises) use `input()` — they'll **pause and wait** for
you to type something and press Enter. That's expected.

Or open the interactive REPL and paste snippets:

```bash
python
>>> "AI" + " " + "Engineer"
'AI Engineer'
```

## Today's exercises
Three of them — see [`exercises/`](exercises/):
1. **Age Calculator** — `input()` + type-casting + f-strings
2. **Shopping Cart** — f-string number formatting (₹ amounts)
3. **Press Release** — cleaning messy text with string methods + chaining

➡ Next: **[Day 03 — Booleans, conditionals & logical operators](../Day-03-Booleans-and-Conditionals/)**
