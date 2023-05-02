import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
choice = int(input())
if choice != 0 and choice != 1 and choice != 2:
    print("Please, choose a valid choice.")
random = random.randint(0, 2)
print("Computer choose: ")
match random:
    case 0:
        print(rock)
    case 1:
        print(paper)
    case 2:
        print(scissors)

match choice:
    case 0:
        if random == 0:
            print("Tie!")
        elif random == 1:
            print("You lose!")
        else:
            print("You win!")
    case 1:
        if random == 0:
            print("You win!")
        elif random == 1:
            print("Tie!")
        else:
            print("You lose!")
    case 2:
        if random == 0:
            print("You lose!")
        elif random == 1:
            print("You win!")
        else:
            print("Tie!")
