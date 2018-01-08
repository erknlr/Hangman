wordlist = loadWords()

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'long.')

    guesses_left = 8
    letters_guessed = list()
        
    while not isWordGuessed(secretWord, letters_guessed):
        print('-------------')
        print('You have ', guesses_left,' guesses left.')
        print('Available letters: ', getAvailableLetters(letters_guessed))
        x = input('Please guess a letter: ').lower()
        
        if x in letters_guessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, letters_guessed))
        elif x in secretWord:
            letters_guessed.append(x)
            print('Good guess: ', getGuessedWord(secretWord, letters_guessed))
        else:
            letters_guessed.append(x)
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, letters_guessed))
            guesses_left -= 1
        
        if isWordGuessed(secretWord, letters_guessed):
            print('-------------')
            print('Congratulations, you won!')
            break
        elif guesses_left < 1:
            print('-------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)