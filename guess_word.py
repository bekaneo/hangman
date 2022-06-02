from random import sample


def get_validated_guess(guessed_letters: str, correct_guesses: str) -> str:
    '''
    Asks users input and returns if input is valid.
    '''
    while True:
        user_guess = input('Enter your guess: ').lower()
        if len(user_guess) != 1:
            print('Enter only 1 letter')
        elif user_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Enter only letter')
        elif user_guess in guessed_letters+correct_guesses:
            print(guessed_letters)
            print(f'You alredy guessed this letter: {user_guess}')
        else:
            return user_guess


def get_random_word(list_words: list) -> str:
    '''
    Returns random word from list of words
    '''
    return sample(list_words, 1)[0]


def hangman(bot_word: str, incorrect_letters: str, correct_guesses: str, tries: int) -> str:
    '''
    Displays tries, guessed letters and returns bots word with correct letters and blank spaces.
    '''
    print(f'You have: {tries} tries')
    print(f'You guessed this letters: {incorrect_letters + correct_guesses}')
    display_word = '*' * len(bot_word)
    i = 0
    while i < len(bot_word):
        if bot_word[i] in correct_guesses:
            display_word = display_word[:i] + bot_word[i] + display_word[i+1:]
        i += 1
    return display_word


words = ['cat', 'ship', 'airplane', 'dog',
         'house', 'phone', 'book', 'notebook']


game_is_on = True
tries = 6
incorrect_letters = ''
correct_guesses = ''
bot_word = get_random_word(words)
while game_is_on:
    display = hangman(bot_word, incorrect_letters, correct_guesses, tries)
    if '*' not in display:
        print(f'You won! The word was: {bot_word}')
        break
    print(display)
    user_guess = get_validated_guess(incorrect_letters, correct_guesses)
    if user_guess in bot_word:
        correct_guesses += user_guess
    else:
        incorrect_letters += user_guess
        tries -= 1
    if tries == 0:
        print(f'You lost, the word was: {bot_word}')
        break
