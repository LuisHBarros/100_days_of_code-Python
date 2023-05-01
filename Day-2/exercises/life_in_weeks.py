"""
Exercise #3
Page of the exercise:
https://app.codingrooms.com/w/94F7C0TVx0jm
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

years = 90 - int(age)
mouths = years * 12
weeks = years * 52
days = years * 365
print(f"You have {days} days, {weeks} weeks, and {mouths} months left.")
