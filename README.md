# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Objective

The main aim of this project was to go over and practice basic Python syntax. It utilises OOP principles and is therefore built around one class,Hangman, which includes three methods:

__init__(self, word_list, num_lives=5), that initialises the attributes as indicated in the docstring;
check_letter(self, letter) -> None, that checks if the input letter provided by the user is in the random word;
ask_letter(self), that asks the user for a letter and checks if this letter has already been tried, and if the input is correct.
Being a command line application, the program can be executed using the Python3 hangman_solution.py command.

Upon initialisation, the user is informed of the length of the randomly selected word to be guessed, which is presented to them as an empty list along the lines of that in the following image.

 ![](hangman_game_three.png)

 The user is then asked to guess a single letter and input it in the programme repeatedly, until they either win or lose the game. Messages are displayed throughout, as I discuss in what follows.

## Milestone 1

The basic logic of the Hangman game was provided in a publicly accessible template by AiCore. Milestone 1 (M1) was straightforward, and is marked in the hangman.solution.py file as # TODO 1. M1 basically only required to modify the ask_letter() method to ask the user to input a letter, store it in a variable called letter, and check whether letter was just one character, or more.

letter = input("Please enter a letter: ")
if len(letter) != 1:
    print("Please, enter just one character")
To test the code, the ask_letter() method can be called within the play_game() function. In case of a wrong input of more than one character, the programme is instructed to print the following message:

    letter = input("Please enter a letter: ")

    if len(letter) != 1:

    print("Please, enter just one character")
