import random
import string

print("Password Generator")

length = int(input("Enter your password length: "))

b = input("Include Uppercase? (yes/no): ").lower()
f = input("Include Lowercase? (yes/no): ").lower()
d = input("Include numbers? (yes/no): ").lower()
e = input("Include symbols? (yes/no): ").lower()

# Build character pool
characters = ""

if b == "yes":
    characters += string.ascii_uppercase

if f == "yes":
    characters += string.ascii_lowercase

if d == "yes":
    characters += string.digits

if e == "yes":
    characters += string.punctuation

# Safety check
if characters == "":
    print("Please select at least one option!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)