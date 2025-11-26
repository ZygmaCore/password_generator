import os
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---
while True:
    print("Welcome to the ZygmaCore Password Generator!")
    input_letter = int(input("How many letters would you like in your password?\n"))
    input_symbol = int(input("How many symbols would you like?\n"))
    input_number = int(input("How many numbers would you like?\n"))

    os.system("clear")

    password = []

    for letter in range(0, input_letter):
        password += random.choice(letters)
    for symbol in range(0, input_symbol):
        password += random.choice(symbols)
    for number in range(0, input_number):
        password += random.choice(numbers)

    print(password)
    random.shuffle(password)
    print(password)

    result = ""
    for final_password in password:
        result += final_password

    print(f"Your password is: {result}")

    retry = input("Wanna Try Again? (Y/N) ")
    if retry == "y":
        os.system("clear")
    elif retry == "n":
        break
    else:
        print("Input Error, Program Stopped!")
        break

print("Have a Nice Day ~~~")