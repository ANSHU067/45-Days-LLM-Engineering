"""
Exercise 2 — BMI Calculator (solution).

Run (asks for input):
    python bmi_calculator_solution.py
"""

# input() is always a string -> cast to float for decimals like 1.75
weight = float(input("Your weight in kg (e.g. 68): "))
height = float(input("Your height in metres (e.g. 1.75): "))

bmi = weight / (height ** 2)        # ** is exponent: height squared

# Checked from lowest to highest. Only the FIRST matching branch runs.
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:                      # we already know bmi >= 18.5 here
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {bmi:.1f} -> {category}")
