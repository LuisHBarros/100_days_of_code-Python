import random
from hangman_art import logo, stages
from hangman_words import word_list
import os

chosen_word = random.choice(word_list)
lives = 6
res = []
for _ in range(len(chosen_word)):
    res += "_"
op = input("Do you use Windows or Linux? (w/l)").lower()
if op == "l":
    clear = "clear"
else:
    clear = "cls"
won = False
print(logo)
while lives > 0 and not won:
    aux = 0
    guess = input("Guess a letter: ").lower()
    os.system(clear)
    if guess in res:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            res[position] = chosen_word[position]
            aux += 1
    if aux == 0:
        lives -= 1
    print(stages[lives])
    print(res)

    if "_" not in res:
        won = True
    print(f"lives = {lives}")

if lives > 0:
    print("Congratulations, you won!")
else:
    print(f"Game over!\nThe world is {chosen_word}")
