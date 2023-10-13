# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
import random
# Step 2: Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Step  3 & 4: Create the random.choice method and pass the word_list variable into the choice method.
word_list = favorite_fruits
word = random.choice(word_list)

# Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)

# Step 6: Using the input function, ask the user to enter a single letter.
guess = input("Please enter a single letter: ")

# Step 7: Assign the input to a variable called guess and print guess variable.
print(guess)


# Step 8: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.

if len(guess) == 1 and guess.isalpha():
    # Step 9: In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    #Step 10: Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
    print("Oops! That is not a valid input.")



def create_word_list():
    favorite_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    return favorite_fruits

def select_random_word(word_list):
    import random
    random_word = random.choice(word_list)
    return random_word

def get_user_input():
    user_guess = input("Please enter a single letter: ")
    return user_guess

def validate_user_input(user_guess):
    if len(user_guess) == 1 and user_guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
