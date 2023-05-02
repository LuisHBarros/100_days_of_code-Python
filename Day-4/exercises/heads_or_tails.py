"""
Exercise #1
Page of the exercise:
    https://app.codingrooms.com/w/Qig4LHBKen17
"""

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

import random


seed = random.randint(1, 2)
if seed == 1:
    print("Heads")
else:
    print("Tails")
