
import random

random_number = random.randint(0, 100)

#print(f"This is my random number: {random_number}")

guesses_allowed = 5
guesses_taken = 0

print("Welcome to the Guess the Number Game!")

print(f"You get {guesses_allowed} guesses. The number will be between 0 and 100. Good luck!")


while guesses_taken < guesses_allowed:
    user_input = int(input("Please enter your guess."))

    if user_input > random_number:
        print("Guess to high.")
    elif user_input < random_number:
        print("Guess to low.")
    else:
        # won the game
        print("Great job! You won the game.")
        break

    guesses_taken += 1

# Check if guesses taken are equal to or greater than guesses_allowed
# If so, then game lost.
if guesses_taken >= guesses_allowed:
    print(f"Sorry you did not guess the number. The number was { random_number }")


