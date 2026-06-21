import random

length = int(input("Enter length: "))

b = input("Uppercase? ").lower()
f = input("Lowercase? ").lower()
d = input("Numbers? ").lower()
e = input("Symbols? ").lower()

characters = ""

if b == "yes":
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if f == "yes":
    characters += "abcdefghijklmnopqrstuvwxyz"

if d == "yes":
    characters += "0123456789"

if e == "yes":
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"

if characters == "":
    print("Select at least one option!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)