"""
Exercise #5
Page of the exercise:
    https://app.codingrooms.com/w/e83fsD4r6O9i
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
true = 0
love = 0

for letter in "true":
    true += name1.lower().count(letter)
    true += name2.lower().count(letter)

for letter in "love":
    love += name1.lower().count(letter)
    love += name2.lower().count(letter)

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
