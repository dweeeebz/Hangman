import random
import tempfile
import time

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # List of words to be used
        self.word = random.choice(word_list) # Mystery word to be guessed
        self.word_guessed= [' '' ' for i in self.word] # Mystery word printed as a list of unknown letters [ _, _, _,...]
        self.num_letters = len(set(self.word)) # Number of letters of mystery word
        self.num_lives = num_lives # Number of lives left after each round
        self.list_of_guesses = []
        print(f"The mystery word has {self.num_letters} characters\n {self.word_guessed}")
        self.pics = {4:'''
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                =========''', 
                3:'''

                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                =========''',

                2:
                
                            '''
                
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                =========''', 1:
                
                            '''   
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                =========''', 
                
                0: '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                ========='''}
        

    def check_guess(self, guess):
            '''
            Checks if the , guess input is in the word.
            If it is, it replaces the ' '' ' in the word_guessed list with the letter.
            If it is not, it reduces the number of lives by 1.
            '''  
            if guess not in self.word:      
                self.num_lives -= 1
                print(f"Sorry, '{guess}' is not in the word.") 
                print(self.pics[self.num_lives])
            else:
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
                print(f"Good guess! '{guess}' is in the word!")
            self.list_of_guesses.append(guess)
            print(f"Mystery word is {self.word_guessed}.  Letters guessed {list(set(self.list_of_guesses))}. You have {self.num_lives} lives left.")         
            

    def ask_for_input(self):
        '''
        Method asks user for input and checks if the input is a valid guess
        '''
        try:
            while True:  
                guess = input("Please enter a letter: ").lower()
                if len(guess) > 1:
                    print("Invalid letter. Please, enter a single alphabetical character.") 
                elif guess.isalpha() == False:
                    print(f"'{guess}' is not a letter.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.list_of_guesses.append(guess)
                    return self.check_guess(guess)  
                break
        except:
            raise Exception

def play_game():
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
   
    game = Hangman(word_list, num_lives=5) # Creating an instance of he Game object

    try:
        game.ask_for_input()
        while True:
            if sorted(game.word_guessed) == sorted(list(game.word)):
                print("Congratulations! You won!")
                break
            elif game.num_lives == 0:
                print(f"You lost! The word was '{game.word}'")
                break
            else:
                game.ask_for_input()
    except:
        pass


play_game()