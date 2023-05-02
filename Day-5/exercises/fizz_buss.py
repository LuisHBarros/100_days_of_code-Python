"""
Exercise #4
Page of the exercise:
    https://app.codingrooms.com/w/BmhHj31MtcB0
"""
for i in range(1, 101):
    response = ""
    if i % 3 == 0:
        response += "Fizz"
    if i % 5 == 0:
        response += "Buzz"
    if response == "":
        response += str(i)
    print(response)
