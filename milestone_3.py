# Task 1: Iteratively check if the input is a valid guess

# Step 1: Create a while loop with condition set to True for continuous execution.
#while True:
    # Step 2: Ask the user to guess a letter and assign it to a variable called guess.
 #   guess = input("Guess a letter: ")

    # Step 3: Check if the guess is a single alphabetical character using isalpha() method.
 #   if guess.isalpha() and len(guess) == 1:
        # Step 4: If the guess passes the checks, break out of the loop.
#        break
 #   else:
 #       # Step 5: If the guess does not pass the checks, print an error message.
 #       print("Invalid letter. Please, enter a single alphabetical character.")

# After the loop, you can use the valid 'guess' variable for further processing.
# print("You guessed:", guess)  # For example, print the valid guess.

# Task 2: Check weather the guess is in the word.

#import random

# Step 1: Create a while loop with condition set to True for continuous execution.
#while True:
    # Step 2: Ask the user to guess a letter and assign it to a variable called guess.
 #   guess = input("Guess a letter: ")

    # Step 3: Check if the guess is in the secret word.
 #   secret_word = random.choice(["apple", "banana", "orange", "mango", "strawberry"])  # Randomly choose a word
 #   if guess in secret_word:
        # If the guess is in the word, print a success message.
   #     print(f"Good guess! '{guess}' is in the word: {secret_word}")
  #      break  # Exit the loop if the guess is correct
   # else:
        # If the guess is not in the word, print an error message and continue the loop.
   #     print(f"Sorry, '{guess}' is not in the word. Try again.")


 # Task 3: Create functions to run the checks

import random

# Step 1: Define the check_guess function and pass in the guess as a parameter.
def check_guess(guess):
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the secret word.
    secret_word = random.choice(["apple", "banana", "orange", "mango", "strawberry"])
    if guess in secret_word:
        # If the guess is in the word, print a success message.
        print(f"Good guess! '{guess}' is in the word: {secret_word}")
        return True  # Return True if the guess is correct
    else:
        # If the guess is not in the word, print an error message and return False.
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

# Step 1: Define the ask_for_input function.
def ask_for_input():
    # Step 2: Move the code that checks if the input is a valid guess into this function.
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            # Step 3: Call the check_guess function to check if the guess is in the word.
            if check_guess(guess):
                break  # Exit the loop if the guess is correct
        else:
            # Print an error message if the guess is not valid and continue the loop.
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test your code.
ask_for_input()
