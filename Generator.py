import random

length = int(input("Enter length: "))

b = input("Uppercase? yes/no?")
c = input("Lowercase? yes/no?")
d = input("Numbers? yes/no?")
e = input("Symbols? yes/no?")

characters = ""

if b == "yes":
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if c == "yes":
    characters += "abcdefghijklmnopqrstuvwxyz"

if d == "yes":
    characters += "0123456789"

if e == "yes":
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"

if characters == "":
    print("Select the options firstly")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
