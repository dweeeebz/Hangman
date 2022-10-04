# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The class Hangman class is defined by 2 methods; check_guess and ask_for_input.
First initialising the below attributes using the __init__ method:
1 - word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

2 - word_guessed: list - A list of the letters of the word, with '' for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

3 - num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

4 - num_lives: int - The number of lives the player has at the start of the game.

5 - word_list: list - A list of words.

6 - list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.


### Milestone 1: Set up the environment

First I created a new repository in GitHub. Here is where code changes are tracked.

### Milestone 2: Create the variables for the game

In Milestone 2 is where the variables were defined. 
        1.) Defining a list of possible words.
        2.) Asking the user for a valid input.

### Milestone 3: Check if the guessed character is in the word
The code for Milestone 3 checks whether each valid input by the user is correct or not.
Setting a loop up in a "While true" statement meant the script will ask the user iteratively until either the word is guessed or the number of lives has reached 0.
In each loop, if the letter guessed is valid breaks the loop.
After each input, the user will see a message printed saying if the input is valid or not or if it is correct.

### Milestone 4: Creating the game class
Firstly I created the class and assigned the class atributes. The __init__ function is called when the instance is created and ready to be initialized. It is an instance method that sets things up in the object.

After the methods are then created to check letters guessed. 

### Milestone5: Putting it all together 
Using Context Managers allowed me to have the user add their list of words they would like to play.
By creating temporary files saves on the processing energy

Notes on Context Managers
Context managers allow for allocation of resources. The [with] statement means that temporary files are automatically closed.
```
Open returns a file object, which has methods and attributes for 
getting information about and manipulating the opened file.
The With function takes care of closing the file automatically.

with tempfile.TemporaryDirectory(dir='.') as tmpdirname:
    print(tmpdirname)
    with open("Words.txt", "a+") as file:
        file.write("Whatever you want to add in the temporary file") # Adding words into a temporary file 
        file.seek(0) # sets Reference point to zeroth index position from the beginning
        words =  file.read()
        words = list(map(str,words.split()))
    time.sleep(20)
```
