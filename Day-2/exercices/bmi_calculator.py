"""
Exercise #2
Page of the exercise:
    https://app.codingrooms.com/w/pwsd6PHyoRUI
"""

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
height = float(height)
weight = float(weight)
# Write your code below this line 👇

bmi = int(weight / (height**2))

print(bmi)
