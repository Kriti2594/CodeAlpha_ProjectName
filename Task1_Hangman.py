import random

words = ["apple", "banana", "mango", "grape", "orange"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display_word = ""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("Already guessed!")
        continue
    
    guessed_letters.append(guess)
    
    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_wrong - wrong_guesses)
    
    if all(letter in guessed_letters for letter in word):
        print("\nYou won! The word was:", word)
        break
else:
    print("\nYou lost! The word was:", word)
