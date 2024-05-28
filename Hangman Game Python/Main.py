# imports

import time
import random
import os
from art import stages
from word import word_list

# Word Selection and setting important variables

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guess_words = set()
end_of_game = False
lives_lost = 0

# introduction

print("Welcome to Hangman")
time.sleep(2)
print("Guess the letters in a random word.")
time.sleep(3)
print("If your letter is actually a part of the word it is added to the spelling.")
time.sleep(3)
print(f'If not. Hangman is slowly led towards death.')
time.sleep(3)
print(f"If you guess a wrong letter 6 times hangman is hung")
time.sleep(3)

os.system('cls')

# Game  starts

print(f'Your word is a {word_length} letter word')

display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:

    guess = input("Guess a letter: ").lower()
        
    os.system('cls')

    print(f"You have guessed the letter {guess}.\n")

    
    if guess in display:
        print(f"You have already guessed {guess}")
    

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    print("\n")
    
    guess_words.add(guess)
    

    
    print("Guessed Letters:")
    print(guess_words)

    
    if guess not in chosen_word:
        print(f"The letter {guess} is not present in the word.\n")
        print("You have lost a life\n")
        lives_lost += 1
        if lives_lost == 6:
            end_of_game = True
            print("You Lose")
            print(f"The word was {chosen_word}\n")
            
    
    if "_" not in display:
        end_of_game = True
        print("You Win!!\n")
        print(f"The word was {chosen_word}\n")

    
    print(stages[lives_lost])