from project_logo import logo

def find_winner(offers):
    biggest_offer = 0
    winner = ""
    for name, bid in offers.items():
        if bid > biggest_offer:
            winner = name
            biggest_offer = bid
    
    return winner, biggest_offer

def clear():
    print("\n" * 100)

print(logo)

offers = {}
should_continue = True

while should_continue:
    name = input("What is your name?\n")
    bid = int(input("What is yout bid?\n$ "))

    offers[name] = bid

    while should_continue:
        other_bidders = input("Are there any other bidders? Type 'Y' or 'N': ").upper()

        if other_bidders == 'N':
            should_continue = False
            break
        elif other_bidders == 'Y':
            clear()
            print(logo)
            break
        else:
            print("Invalid input. You need to choose 'Y' or 'N'.")

winner, biggest_offer = find_winner(offers)
print(f"The winner is {winner} with a bid of $ {biggest_offer}") 
    