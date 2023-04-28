"""
Project #2: Tip Calculator
Project Page:
https://app.codingrooms.com/w/DgNBTEG8S7uo
"""


print("Welcome to the tip calculator")
total = input("What was the total bill? ")
total = float(total)
people = input("How many people to split the bill? ")
people = float(people)
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip = float(tip)
value = total / people
value += round(value * tip / 100, 2)
print(f"Each person should pay: ${value}")
