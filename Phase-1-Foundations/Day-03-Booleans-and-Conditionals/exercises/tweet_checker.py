"""
Exercise 1 — Tweet Checker (STUDENT STUB).

A tweet is valid only if it is 1-280 characters long (and not empty).
Tell the user whether their tweet can be posted, and by how much it's over/under.

Run (asks for input):
    python tweet_checker.py
"""

MAX_LEN = 280

tweet = input("Type your tweet: ")

# TODO 1: get the length of the tweet with len()
# length = ...

# TODO 2: handle the empty case first (an empty string is falsy!)
#         if not tweet:  -> print "Your tweet is empty!"

# TODO 3: elif the length is within 1..280 -> print "✅ Good to post! (N/280 chars)"

# TODO 4: else (too long) -> tell them how many characters OVER they are
#         over = length - MAX_LEN
