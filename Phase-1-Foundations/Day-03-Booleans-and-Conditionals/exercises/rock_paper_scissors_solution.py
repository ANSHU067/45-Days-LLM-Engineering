"""
Exercise 3 — Rock, Paper, Scissors vs the Computer (solution).

Run (asks for input):
    python rock_paper_scissors_solution.py
"""

import random

OPTIONS = ["rock", "paper", "scissors"]

# .strip().lower() makes "  Rock " match "rock" (Day 2 string methods!)
player = input("rock, paper or scissors? ").strip().lower()

# Validate input before doing anything else
if player not in OPTIONS:
    print(f"'{player}' isn't a valid move. Choose rock, paper or scissors.")
else:
    computer = random.choice(OPTIONS)
    print(f"You chose {player}, computer chose {computer}.")

    # The three combinations where the PLAYER wins
    player_wins = (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    )

    if player == computer:
        print("It's a draw!")
    elif player_wins:
        print("You win!")
    else:
        print("Computer wins!")
