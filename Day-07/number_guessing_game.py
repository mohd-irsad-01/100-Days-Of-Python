# Number Guessing Game using while loop
import random

secret_number = random.randint(1, 100)
guess = 0

print("Guess the number between 1 to 100! ")

while guess != secret_number:
    guess = int(input("Enter your guess number: "))
    if guess < secret_number:
        print("Too low! Try again")
    elif guess > secret_number:
        print("Too high! Try again")
    else:
        print(f"Congratulations! You guessed it, number was {secret_number}")
