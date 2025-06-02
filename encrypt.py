import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

def encrypt():
    user_input = input("Type a phrase you want to shuffle: ")
    cipher_text = ""

    for char in user_input:
        index = chars.index(char)
        cipher_text += key[index]

    print(f"Your shuffled text is: {cipher_text}.")
    #print(f"Chars: {chars}")
    #print(f"Key: {key}")

def decrypt():
    user_input = input("What phrase would you like to decrypt: ")
    plain_text = ""

    for char in user_input:
        index = key.index(char)
        plain_text += chars[index]
    print(f"Your decrypted text is: {plain_text}.")

def main():
    while True:
        what_to_do = input("Would you like to encrypt or decrypt (e/d/q): ")
        match what_to_do:
            case "e":
                encrypt()
            case "d":
                decrypt()
            case "q":
                print("Goodbye!")
                break
            case _:
                print("Huh?")

main()