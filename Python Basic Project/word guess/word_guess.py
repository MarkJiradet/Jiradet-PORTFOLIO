"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random

LEXICON_FILE = "Lexicon.txt"
   
INITIAL_GUESSES = 8             


def play_game(word):
    
    global INITIAL_GUESSES
    
    secret_word = ''  

    used_word =''
   
    while INITIAL_GUESSES > 0:  
    
        print ("The word now look like this: ", end ='')  
       
        for char in word:    
            if char in secret_word:       
                print(char, end = '')     
            else:       
                print("-", end = '')            
                
        print("\nYou have",INITIAL_GUESSES,"guesses left")  
        
        if used_word != '':
            print("You past guesses are",used_word)
            
        alphabet = input("Type a single letter here,then press enter: ")  
        alphabet= alphabet.upper()
        
        if len(alphabet)==1:
            used_word += alphabet
            if alphabet not in word:  
                INITIAL_GUESSES -= 1  
                print("There are no",alphabet,"'s in the word.")  
                if INITIAL_GUESSES == 0:  
                    print("Sorry, you lost. The secret word was:",word)
            elif alphabet in word:
                secret_word += alphabet  
                print("That guess is correct.")  
                if secret_word == word:
                    print("Congratulations, the word is:",word)
                    break
        elif len(alphabet)>1:
            print("A guess should be a single character.")
        
        print("\n")


def get_word():
    
    global LEXICON_FILE
    
    f = open(LEXICON_FILE, 'r')
    
    data = f.read().strip().split("\n")
    
    index = random.randrange(len(data))
    
    return data[index]

def main():

    word = get_word()
    play_game(word)

if __name__ == "__main__":
    main()