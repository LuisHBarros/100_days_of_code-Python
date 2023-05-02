"""
Exercise #2
Page of the exercise:
    https://app.codingrooms.com/w/625t77J5kGqg
"""


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

higher = student_scores[0]
for value in student_scores:
    if value > higher:
        higher = value
print(f"The highest score in the class is: {higher}")
