import random
from project_logo import logo

def clear():
    print("\n" * 100)

def deal_card():
    """Return a random card from the desk"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if  11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif user_score > 21 and computer_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        while True:
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
                break
            else:
                user_should_deal = input("Type 'Y' to get another card or type 'N' to pass: ").upper()
                if user_should_deal == 'Y':
                    user_cards.append(deal_card())
                    break
                elif user_should_deal == 'N':
                    is_game_over = True
                    break
                else:
                    print("Invalid input. You need to choose 'Y' or 'N'.")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final_score: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").upper()
    if play_again == "Y":
        clear()
        play_game()
    elif play_again == "N":
        print("Goodbye! :)")
        break
    else: 
        print("Invalid input. You need to choose 'Y' or 'N'.")
