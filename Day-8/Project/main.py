"""
Caesar Cipher
"""
from alphabet import alphabet
from art import logo


def ceaser(start_text: str, shift_amount: int, cipher_direction: str) -> str:
    while True:
        if cipher_direction == "decode":
            return decode(start_text, shift_amount)
        elif cipher_direction == "encrypt":
            return encrypt(start_text, shift_amount)
        else:
            print(
                "Unknown cipher_direction! Please, enter a valid cipher_direction(decode/encrypt)"
            )


def encrypt(message: str, shift: int) -> str:
    res = ""
    for letter in message:
        res += alphabet[alphabet.index(letter.lower()) + shift]
    return res


def decode(message: str, shift: int) -> str:
    res = ""
    for letter in message:
        res += alphabet[alphabet.index(letter.lower()) - shift]
    return res


def main():
    print(logo)
    choose = ""
    while choose != "n":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n")) % 26
        if direction == "encode":
            result = encrypt(text, shift)
        else:
            result = decode(text, shift)
        print(result)
        while True:
            choose = input("Do you want to go again? (y/n): ")
            if choose == "y" or choose == "n":
                break
            print("Please, enter your choice correctly!\n")


if __name__ == "__main__":
    main()
