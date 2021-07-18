import random as ran
import re   # Regular expresions

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
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    
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

def word_with_gaps_to_regex(word: str) -> re:
    return re.compile(word.replace("_ ", ".") + "$")

def list_to_str(l: list, s = '') -> str:
    return s.join(str(i) for i in l)

def get_total_score(guesses_remaining: int, secret_word: str) -> int:
    num_unique_letters = len(set(secret_word))
    return guesses_remaining * num_unique_letters

def match_with_gaps(my_word, other_word) -> bool:
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    return bool(word_with_gaps_to_regex(my_word).match(other_word))

def show_possible_matches(my_word, wordlist: list):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    word_regex = word_with_gaps_to_regex(my_word)
    matches = list(filter(word_regex.match, wordlist))
    if len(matches) != 0:
        print(list_to_str(matches, s=" "))
    else:
        print("No matches found ")