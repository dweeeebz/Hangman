# %%

import tempfile
import time
import random


with tempfile.TemporaryDirectory(dir='.') as tmpdirname:
    print(tmpdirname)
    with open("Words.txt", "a+") as file:
        file.write("apple\npear\nwatermellon\ncat\n") # Adding words into temporary file 
        file.seek(0) # sets Reference point to zeroth index position from the beginning
        words =  file.read()
        words = list(map(str,words.split()))
    time.sleep(20) # Observe the current directory during these 20 seconds
                   # Inside that directory you will find the words.txt file
                   # After 20 seconds, *puff* gone!

word = random.choice(words)

'''
while True:
    guess = input("Please enter a letter: ").lower()
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
'''

# Correct check_function
def check_guess(guess): # Function checks if the guess is in the word
    #guess = input("Please enter a letter: ")
    try:
        guess = guess.lower()
        if guess not in word:
            print(f"Sorry, '{guess}' is not in the word. Try again.") 
            
        else:
            print(f"Nice! '{guess}' is in the word!")
        return True     
    except:
        pass

def ask_for_input(guess): #Function checks if input is valid or not
    #check_guess(guess)
    try:
        while True:
            guess = input("Please enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha() == True:
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")  
        check_guess(guess)             
    except:
        pass

# %%
