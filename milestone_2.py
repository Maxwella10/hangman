# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
import random
# Step 2: Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Step  3 & 4: Create the random.choice method and pass the word_list variable into the choice method.
word_list = favorite_fruits
word = random.choice(word_list)

# Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)