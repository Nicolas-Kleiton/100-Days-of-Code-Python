from project_logo import logo
from random import randint

EASY_LEVEL = 5
HARD_LEVEL = 10

def clear():
    print("\n" * 100)

def number_generator():
    return randint(1, 100)

def play():
    while True:
        play = input("\nDo you want to play? Type 'Y' or 'N': ").upper()

        if play == 'Y':
            return True
        elif play == 'N':
            print("\nGoodbye! 🎉")
            return False
        else:
            print("\nInvalid input. Please type 'Y' or 'N'.")
    
def set_difficulty():
    while True:
        difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty == 'easy':
            return EASY_LEVEL
        elif difficulty == 'hard':
            return HARD_LEVEL
        else:
            print("\nInvalid input. Please type 'easy' or 'hard'.")

while play():
    clear()
    number = number_generator()
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I am thinking in a number between 1 and 100.")

    attempts = set_difficulty()

    while attempts != 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number!")

        while True:
            try:
                guess = int(input("\nMake a guess: "))
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        if guess > number:
            print("Too high! Guess again.")
        elif guess < number:
            print("Too low! Guess again.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {number} correctly!")
            break

        attempts -= 1

    if attempts == 0:
        print(f"\n😕 You've run out of guesses. The correct number was {number}. Better luck next time!")    
