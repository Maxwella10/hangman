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
