# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            if i != len(secretWord) - 1:
                continue
            else:
                return True
        else:
            return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            s = s + secretWord[i]
        else:
            s = s + '_'
    return s
            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    s = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        if letter in s:
            s = s.replace(letter,"")
    return s
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    mistakesMade = 0
    warning = 3
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("You have " + str(warning)+" warnings left")
    while not (isWordGuessed(secretWord, lettersGuessed)) and mistakesMade < 6:
        print("-----------")
        #print("You have " + str(warning)+" warnings left")
        print("You have " + str(6-mistakesMade) + " guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed), end="")
        letter = input("Please guess a letter: ")
        if not letter.isalpha():
            warning -= 1
            print("Oops! That is not a valid letter.", end = "")      
            if warning < 0:
                mistakesMade += 1
                print("You have no warnings left so you lose one guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:   
                print("You have "+ str(warning)+" warnings left: "+ getGuessedWord(secretWord, lettersGuessed))              
            continue
            
        letter = letter.lower()
        if letter in secretWord and letter not in lettersGuessed:
            lettersGuessed = lettersGuessed + [letter]
            print("Good Guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif letter in lettersGuessed:
            warning -= 1
            print("Oops! You've already guessed that letter.", end = "")
            if warning < 0:
                mistakesMade += 1
                print("You have no warnings left so you lose one guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:   
                print("You have "+ str(warning)+" warnings left: "+ getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed = lettersGuessed + [letter]
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            if(letter in ['a', 'e', 'i', 'o', 'u']):
                mistakesMade += 2
            else:
                mistakesMade += 1
        ###
    print("-----------")
    if mistakesMade == 6:
        print("Sorry, you ran out of guesses. The word was " + secretWord)
    else:
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str((6-mistakesMade)* len(set(secretWord))))
            
    
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = 'else'
hangman(secretWord)
