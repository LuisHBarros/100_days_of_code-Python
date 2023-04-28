"""
Project #1: band-name-generator-end
Project page:
    https://app.codingrooms.com/management/assignments/577105/overview
"""

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print(f"Your band name could be {city + ' ' + pet}")


class Vampire:
    name: str
    age: int
    bloodType: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
