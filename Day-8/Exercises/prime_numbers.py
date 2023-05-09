# Write your code below this line 👇

import math


def prime_checker(number) -> bool:
    square = int(math.sqrt(number)) + 1
    for i in range(2, square):
        if number % i == 0:
            print("It's not a prime number.")
            return False
    print("It's a prime number.")
    return True


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
