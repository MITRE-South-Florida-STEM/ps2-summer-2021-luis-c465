# %%

# Problem Set 2, hangman.py
# Name: Luis Canada
# Collaborators: None
# Time spent: ???

import gameutilities as util

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = util.load_words()

def hangman(secret_word):
    '''Starts up an interactive game of Hangman.

    secret_word: string, the secret word to guess.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    user_guesses = 6
    user_warnings = 3
    letters_guessed = []

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {user_warnings} warnings left")

    while not util.is_word_guessed(secret_word, letters_guessed) and user_guesses > 0:
        print("-------------")
        print(f"You have {user_guesses} guesses left.")
        # String of all letters available, no spaces
        letters_available = util.list_to_str(util.get_available_letters(letters_guessed))
        print(f"Available letters: {letters_available}")

        guess = util.get_user_guess()
        guessed_word = util.get_guessed_word(secret_word, letters_guessed)

        # TODO: Clean up this code
        if guess in letters_guessed:
            user_warnings, user_guesses = util.update_warning_and_guesses(user_warnings, user_guesses)
            
            print(f"Oops! You've already guessed that letter. You have {user_warnings} warnings left: {guessed_word}")
        elif not guess.isalpha():
            user_warnings, user_guesses = util.update_warning_and_guesses(user_warnings, user_guesses)
            print(f"Oops! That is not a valid letter. You have {user_warnings} warnings left: {guessed_word}")
        elif guess in secret_word:
            # Must update letters guessed to find guessed word
            letters_guessed.append(guess)
            guessed_word = util.get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess!: {guessed_word}")
            continue
        else:
            if util.is_vowel(guess):
                user_guesses -= 2
            else:
                user_guesses -= 1
            
            print(f"Oops! That letter is not in my word.\nPlease guess a letter: {guessed_word}")
        
        letters_guessed.append(guess)

    if util.is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! ")
        score = util.get_total_score(user_guesses, secret_word)
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    user_guesses = 6
    user_warnings = 3
    letters_guessed = []

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {user_warnings} warnings left")

    while not util.is_word_guessed(secret_word, letters_guessed) and user_guesses > 0:
        print("-------------")
        print(f"You have {user_guesses} guesses left.")
        # String of all letters available, no spaces
        letters_available = util.list_to_str(util.get_available_letters(letters_guessed))
        print(f"Available letters: {letters_available}")

        guess = util.get_user_guess()
        guessed_word = util.get_guessed_word(secret_word, letters_guessed)

        # Hint addition
        if guess == "*":
            print("Possible word matches are: ")
            util.show_possible_matches(guessed_word, wordlist)
            continue

        # TODO: Clean up this code
        if guess in letters_guessed:
            user_warnings, user_guesses = util.update_warning_and_guesses(user_warnings, user_guesses)
            
            print(f"Oops! You've already guessed that letter. You have {user_warnings} warnings left: {guessed_word}")
        elif not guess.isalpha():
            user_warnings, user_guesses = util.update_warning_and_guesses(user_warnings, user_guesses)
            print(f"Oops! That is not a valid letter. You have {user_warnings} warnings left: {guessed_word}")
        elif guess in secret_word:
            # Must update letters guessed to find guessed word
            letters_guessed.append(guess)
            guessed_word = util.get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess!: {guessed_word}")
            continue
        else:
            if util.is_vowel(guess):
                user_guesses -= 2
            else:
                user_guesses -= 1
            
            print(f"Oops! That letter is not in my word.\nPlease guess a letter: {guessed_word}")
        
        letters_guessed.append(guess)

    if util.is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! ")
        score = util.get_total_score(user_guesses, secret_word)
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    secret_word = util.choose_word(wordlist)
    secret_word = "apple"
    print("Welcome to the game Hangman! ")

    # hangman(secret_word)
    hangman_with_hints(secret_word)

# %%
