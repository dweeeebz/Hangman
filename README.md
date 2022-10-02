# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Milestone 1: Set up the environment

Created a new repository in GitHub

Milestone 2: Complete the ask_letter method
```
def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        try:
             #while self.num_lives != 0 :
                letter = input("Please enter a letter ").lower()
                self.letter = letter
                if len(letter) > 1:
                    print(f"Please, enter just one character. Letters guessed {list(set(self.list_letters))}") 
                    # break
                elif letter in self.list_letters:
                    print(f"{letter}  was already tried. Letters guessed {list(set(self.list_letters))}") 
                else:
                    #self.list_letters.append(letter)
                    if self.check_letter(letter) == True:
                        print(f"Nice! '{letter}' is in the word! {self.word_guessed}")
                    else:
                        print(f"Sorry, '{letter}' is not in the word. You have {self.num_lives} lives left.")            
        except:
            #print("Game Over")
            raise Exception
```

Milestone 3: Define the initializer & Milestone 4: Complete the "ask_letter" method

```
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {num_letters} characters"
        # 2. {word_guessed}
        # Save variables as attributes
        self.word_list = word_list # List of words to be used
        self.word = random.choice(word_list) # Mystery word to be guessed
        self.word_guessed= ['_' for i in self.word] # Mystery word printed as a list of unknown letters [ _, _, _,...]
        self.num_letters = len(self.word) # Number of letters of mysstery word
        self.num_lives = num_lives # Number of lives left after each round
        self.list_letters = []
        print(f"The mystery word has {self.num_letters} characters\n {self.word_guessed}")
```


Milestone5: Putting it all together 

Context Managers
Creating temporary files to save processing energy

'''
Open returns a file object, which has methods and attributes for 
getting information about and manipulating the opened file.
The With function takes care of closing the file automatically.
'''
with tempfile.TemporaryDirectory(dir='.') as tmpdirname:
    print(tmpdirname)
    with open("Words.txt", "a+") as file:
        file.write("Whatever you want to add in the temporary file") # Adding words into temporary file 
        file.seek(0) # sets Reference point to zeroth index position from the beginning
        words =  file.read()
        words = list(map(str,words.split()))
    time.sleep(20)
```
The class Hangman class is defined by 2 methods; check_guess and ask_for_input.
First initilising the below attributes using the __init__ method:
    1 - word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

    2 - word_guessed: list - A list of the letters of the word, with '' for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

    3 - num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

    4 - num_lives: int - The number of lives the player has at the start of the game.

    5 - word_list: list - A list of words.

    6 - list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.

word_list and num_lives are passed as parameters.

Lastly creating methods to for running the checks
check_guess method checks whether the input is in the word or not. 
ask_for_input method checks if the input is a valid inpiut.

User can define which words the game can choose by running milestone_3 module and inputing the list of words.

Below block of code only runs directly in the module. Otherwise if the module is imported users can decide on what the word list will be.
if __name__ == '__main__': # This line checks if its directly being run by python or run by import.
        word_list = ['blueberry', 'banana', 'apricot', 'grape', 'watermelon']
else: # Runs in modles outside of this script.
with tempfile.TemporaryDirectory(dir='.') as tmpdirname:
    with open("Words.txt", "a+") as file:
        user_words = str(input("Enter a list of words seperated by a ," ))
        file.write(user_words.split()[0]) 
        #file.write("apple\npear\ndog\ncat\n") 
        file.seek(0) 
        words =  file.read()
        word_list = list(map(str,words.split()))
    time.sleep(20)
