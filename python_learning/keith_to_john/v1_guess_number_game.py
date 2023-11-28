
import random

random_number = random.randint(0, 100)

#print(f"This is my random number: {random_number}")

guesses_allowed = 5
guesses_taken = 0

print("Welcome to the Guess the Number Game!")

print(f"You get {guesses_allowed} guesses. The number will be between 0 and 100. Good luck!")


while guesses_taken < guesses_allowed:
    user_input = input(int("Please enter your guess."))
    guesses_taken += 1
    if user_input > random_number:
        print("Guess to high. Guess again.")
    elif user_input < random_number:
        print("Guess to low. Guess again.")
    else:
        if guesses_allowed >= guesses_taken:
            # Out of guesses
            print("you did not win.")
            break
        else:
            # won the game
            print("Great job! You won the game.")




