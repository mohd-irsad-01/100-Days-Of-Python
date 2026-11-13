import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

use_uppercase = input("Include uppercase letters ? (yes/no): ").lower()
use_number = input("Include numbers ? (yes/no): ").lower()
use_symbols = input("Include special characters ? (yes/no): ").lower()

characters = string.ascii_letters

if use_uppercase == "yes":
    characters += string.ascii_letters

if use_number == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

if length < 1:
    print("Invalid password length")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

print("\nYour Generated Password: ", password)
