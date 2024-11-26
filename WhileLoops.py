### Part Two -- 
import random

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)

print("Welcome to the guessing game! Guess a number between 1 and 100.")

while True:
    # Ask the user to input their guess
    guess = int(input("Enter your guess: "))

    if guess < correct_number:
        print("Too low! Try again.")
    elif guess > correct_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break  # Exit the loop when the correct number is guessed
