import random

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_'*len(word)
    guessed = False
    guessed_letters =[]
    guessed_words = []
    tries = 6
    print('Lets play Hangman!')
    print(display_completion(tries))    