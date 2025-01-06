import random
from hangman_words import word_list
from hangman_prints import stages, logo

print(logo)

chosen_word = random.choice(word_list)
display = []

display = ["_" for _ in chosen_word]
attempts = []
lives = 6

while '_' in display and lives > 0:
    print(f"\nCurrent Word: {''.join(display)}") 
    print(f"\nLives remaining: {lives}")
    guess = input("Guess a letter: ").strip().lower()

    if guess in attempts:
        print("You already chose this letter. Try again.")
        continue

    attempts.append(guess)

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else: 
        lives -= 1;
        print("Wrong, you lose a life!")
    
    print(stages[lives])

if "_" not in display:
    print(f"\nCongratulations! You guessed the word: {''.join(display)} :)")
else:
    print(f"\nYou lose! The word was: {chosen_word} :(")
