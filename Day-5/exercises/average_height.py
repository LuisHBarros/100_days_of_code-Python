"""
Exercise #1
Page of the exercise:
    https://app.codingrooms.com/w/PSfHA6mhiFE6
"""
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
lenght = 0
total = 0

for value in student_heights:
    total += value
    lenght += 1

average = round(total / lenght)
print(average)
