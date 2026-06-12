"""
Exercise 3 — Rock, Paper, Scissors vs the Computer (STUDENT STUB).

Rules: rock beats scissors, scissors beats paper, paper beats rock.

Run (asks for input):
    python rock_paper_scissors.py
"""

import random

OPTIONS = ["rock", "paper", "scissors"]

# TODO 1: get the player's move with input(). Lower-case it so "Rock" == "rock".
#         player = input("rock, paper or scissors? ").strip().lower()

# TODO 2: validate it. If player not in OPTIONS -> print an error and stop.

# TODO 3: let the computer pick with random.choice(OPTIONS). Print both moves.

# TODO 4: decide the winner with if / elif / else:
#         - if player == computer -> "Draw"
#         - the three winning combos for the player (use `and`/`or`)
#         - else -> computer wins
