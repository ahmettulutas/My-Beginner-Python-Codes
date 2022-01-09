# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:22:29 2021

@author: Ahmet
"""
import random

WORDLIST_FILENAME = "words2.txt"

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
    for i in list(secretWord):
        if i in lettersGuessed:
            True
        else:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    ans = []
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            ans = ans + ['_']
        else:
            ans = ans + [list(secretWord)[i]]
    return ' '.join(ans)


def getAvailableLetters(lettersGuessed):
    import string
    lowercase = list(string.ascii_lowercase)
    for i in range(len(lettersGuessed)): lowercase.remove(lettersGuessed[i])
    return ''.join(lowercase)


def hangman(secretWord):
    mistakesMade = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guess = ''
    guessLower = guess.lower()
    print('Welcome to the game Hangman!', end='\n'
    'I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    while mistakesMade != 0:
        print('\n------------', end='\n'
              'You have '+str(mistakesMade)+' guesses left.\n'
              'Available letters: '+availableLetters)
        guess = input('Please guess a letter: ')
        guessLower = guess.lower()
        if guessLower in lettersGuessed:
            print("Oops! You've already guessed that letter: "+\
                  getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed = lettersGuessed + [guessLower]
            availableLetters = getAvailableLetters(lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed):
                print("Good Guess: "+ secretWord+'\n'
                      "------------\nCongratulations, you won!")
                return
            elif guessLower in secretWord:
                print("Good Guess: "+getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: "+\
                  getGuessedWord(secretWord, lettersGuessed))
                mistakesMade -= 1
    print("\n------------\n"
          "Sorry, you ran out of guesses. The word was "+secretWord+".")
hangman(chooseWord(wordlist))