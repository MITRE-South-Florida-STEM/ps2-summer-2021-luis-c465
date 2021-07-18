import random as ran

def load_words(WORDLIST_FILENAME = "words.txt") -> list:
    """Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        line = inFile.readline()    # line: string
        wordlist = line.split()     # wordlist: list of strings
        print("  ", len(wordlist), "words loaded.")
    
    return wordlist

def choose_word(wordlist) -> str:
    """Returns a word from wordlist at random

    wordlist (list): list of words (strings)
    """
    return ran.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed) -> bool:
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed) -> str:
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    
    return guessed_word

def get_english_alphabet() -> str:
    return "abcdefghijklmnopqrstuvwxyz"

def get_available_letters(letters_guessed) -> str:
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # Filter out all letters of letters_guessed of the lowercase english alphabet
    return list( filter( lambda a: a not in letters_guessed, get_english_alphabet() ) )

def get_user_guess(input_msg = "Please guess a letter: ") -> str:
    return input(input_msg).lower()

def is_vowel(letter) -> bool:
    return letter in ['a', 'e', 'i', 'o']

def update_warning_and_guesses(warning: int, guesses: int) -> tuple:
    '''Update warning and guesses values

    returns: Tuple where value1 is the warning and value2 is the guesses
    '''
    if warning >= 1:
        return (warning - 1, guesses)
    else:
        return (warning, guesses - 1)

def match_with_gaps(my_word, other_word) -> bool:
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word) != len(other_word):
        return False
    
    for letter in my_word:
        if letter != '_' and letter != other_word:
            return False
    
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    pass