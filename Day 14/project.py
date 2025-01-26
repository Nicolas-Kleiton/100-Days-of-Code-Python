import random
import os

from project_logo import logo, vs
from game_data import data

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def check_answer(A_followers, B_followers, score):
    
    while True:
        answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if answer == 'A' and A_followers > B_followers or answer == 'B' and A_followers < B_followers:
            score += 1
            print(f"\nYou're right! Current score: {score}")
            return score
        elif answer == 'A' and A_followers < B_followers or answer == 'B' and A_followers > B_followers:
            print(f"\nSorry, that's wrong! Final score: {score}")
            return False
        else:
            print("\nInvalid input. Please type 'A' or 'B'.")

while play():

    score = 0
    A = random.choice(data)

    while True:
        clear()
        print(logo)
        print(f"Current score: {score}")

        B = random.choice(data)
        
        while B == A:
            B = random.choice(data)

        A_followers = A['follower_count']
        B_followers = B['follower_count']
 
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

        score = check_answer(A_followers, B_followers, score)

        if not score:
            break
        else:
            A = B
    