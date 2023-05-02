"""
Exercise #2
Page of the exercise:
    https://app.codingrooms.com/w/jhByQ1qwgPaf
"""

# Import the random module here

# Split string method
import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lenght = len(names)
r = random.randint(0, lenght - 1)
print(f"{names[r]} is going to buy the meal today!")
