# Task 1: Create the hangman class
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []



# Task 2: Create methods for running the checks

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


# Example Usage:
word_list =  ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']

hangman_game = Hangman(word_list)

hangman_game.ask_for_input()  # Call the ask_for_input method to test your code


# Task 3: Define what happens if the letter is in the word

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]
        self.num_letters = len(set([letter.lower() for letter in self.word if letter.isalpha()]))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guessed letter to lower case
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess  # Replace "_" with the guessed letter
            self.num_letters -= 1  # Reduce the number of remaining letters to guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
        # You can add logic for checking win/lose conditions here in the future

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  # Call the check_guess method
                self.list_of_guesses.append(guess)  # Append the guess to list_of_guesses
                break

# Example Usage:
word_list =  ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']

hangman_game = Hangman(word_list)

hangman_game.ask_for_input()  # Call the ask_for_input method to test your code
print("Word Guessed So Far: ", hangman_game.word_guessed)
print("Number of Remaining Letters to Guess: ", hangman_game.num_letters)


# Define what happens if the letter is NOT in the word.



import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]
        self.num_letters = len(set([letter.lower() for letter in self.word if letter.isalpha()]))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guessed letter to lower case
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess  # Replace "_" with the guessed letter
            self.num_letters -= 1  # Reduce the number of remaining letters to guess
        else:
            self.num_lives -= 1  # Reduce num_lives by 1 if guess is incorrect
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            # You can add logic for checking win/lose conditions here in the future

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  # Call the check_guess method
                self.list_of_guesses.append(guess)  # Append the guess to list_of_guesses
                break

# Example Usage:
word_list =  ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
hangman_game = Hangman(word_list)

hangman_game.ask_for_input()  # Call the ask_for_input method to test your code
print("Word Guessed So Far: ", hangman_game.word_guessed)
print("Number of Remaining Letters to Guess: ", hangman_game.num_letters)
print("Number of Lives Left: ", hangman_game.num_lives)
