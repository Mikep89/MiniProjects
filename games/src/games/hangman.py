from random import choice

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
        '''
        
            +-----------+
            ||
            ||
            ||
            ||
            ||
            ||
            ||
        ======================''', 
        '''
        
            +-----------+
            ||          |
            ||          O
            ||
            ||
            ||
            ||
            ||
        ======================''',
        '''
        
            +-----------+
            ||          |
            ||          O
            ||          |
            ||
            ||
            ||
            ||
        ======================''',
        '''
        
            +-----------+
            ||          |
            ||          O
            ||         -|
            ||
            ||
            ||
            ||
        ======================''',
        '''
        
            +-----------+
            ||          |
            ||          O
            ||         -|-
            ||
            ||
            ||
            ||
        ======================''',
        '''
        
            +-----------+
            ||          |
            ||          O
            ||         -|-
            ||         /
            ||
            ||
            ||
        ======================''',
        '''
        
            +-----------+
            ||          |
            ||          O
            ||         -|-
            ||         / \\
            ||
            ||
            ||
        ======================'''

    ]

def game():
    dictionary = ['gnu','kernel','linux','megeia','penguin','ubuntu']
    word = choice(dictionary)
    clue = len(word) * ['_']
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and (''.join(clue) != word):
        letters = guess_letter()
        

def scores():

def start():
    print('Lets play a game of Hangman!')
    while game():
        pass
    scores()
