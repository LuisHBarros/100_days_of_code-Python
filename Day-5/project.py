import random
import secrets
import string


print("Wellcome to the PyPassword generator!")
password_lenght = int(input("How many characters do you want in your password? "))
password = []
choice = input("Do you want some letters and special characters? (y/n): ")
if choice == "y":
    half = int((password_lenght - 1) / 2)
    for i in range(half):
        password.append(secrets.choice(string.ascii_letters + string.punctuation))
    for i in range(password_lenght - 1 - half):
        rand = random.randint(0, 9)
        password.append(str(rand))
    random.shuffle(password)
    print(f"Here is your password: {''.join(password)}")

elif choice == "n":
    for i in range(password_lenght - 1):
        rand = random.randint(0, 9)
        password.append(str(rand))
    print(f"Here is your password: {''.join(password)}")
else:
    print("Sorrry, invalid choice!\nTry again, please")
