# Step 1: Create a while loop with condition set to True for continuous execution.
while True:
    # Step 2: Ask the user to guess a letter and assign it to a variable called guess.
    guess = input("Guess a letter: ")

    # Step 3: Check if the guess is a single alphabetical character using isalpha() method.
    if guess.isalpha() and len(guess) == 1:
        # Step 4: If the guess passes the checks, break out of the loop.
        break
    else:
        # Step 5: If the guess does not pass the checks, print an error message.
        print("Invalid letter. Please, enter a single alphabetical character.")

# After the loop, you can use the valid 'guess' variable for further processing.
print("You guessed:", guess)  # For example, print the valid guess.

