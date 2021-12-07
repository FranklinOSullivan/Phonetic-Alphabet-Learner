# Function to help the user learn the phonetic alphabet through the use of a basic python program.

# Import the random library to use within the code
import random

# Make a list of words, representing all of the words within the phonetic alphabet
words_list = ['alpha', 'beta', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu']

# Ask the user if they are playing
playing = input("Would you like to play a round? (y/n) ")
# If the user is playing
while ((playing == 'y') or (playing == 'Y')):
    # Print an empty line
    print()
    # Choose a random word from the list
    word = random.choice(words_list)
    # Tell the user the first letter of the word
    print("The letter is ", word[0])
    # Take their input as a attempt
    attempt = input("What is the phonetic word for this letter? ")
    # If their attempt is equal to the word
    if (attempt == word):
        # Print correct
        print("correct!")
        # If their attempt is different to the word
    else:
        # Print that they were incorrect and print the correct ansert
        print("Incorrect. The correct word was", word)
    # Ask the user if they would like to play another round
    playing = input("Would you like to play another round? (y/n) ")