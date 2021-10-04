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
    word_length = len(word)
    clue = word_length * ['_']
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and (''.join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != 1:
                print(f"You've already picked {letter}")
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print(f"Sorry {letter} isn't what we're looking for.")
                else:
                    print(f'Congratulations! {letter} is correct.')
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print('Choose another letter.')
        hangedman(letters_wrong)
        print(" ".join(clue))
        print(f"Guesses:  {letters_tried}")

        if letters_wrong == tries:
            print("Game Over.")
            print(f"The word was: {word}")
            break
        if "".join(clue) == word:
            print("You win!")
            print(f"The word was: {word}")
            player_score += 1
            break
        return play_again()

def guess_letter():
    letter = input("Take a guess at our mystery word:")
    letter.strip()
    letter.lower()
    return letter

def play_again():
    answer = input("Would you like to play again? y/n")
    if answer.upper() in ("Y","YES",', "OF COURSE!'):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")

def scores():
    global player_score, computer_score
    print('HIGH SCORES')
    print(f'Player: {player_score}')
    print(f'Computer: {computer_score}')

def start():
    print('Lets play a game of Hangman!')
    while game():
        pass
    scores()
