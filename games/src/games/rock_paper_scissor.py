import random
import time

rock, paper, scissors = (1, 2, 3)
names = { rock: "Rock", paper: "Paper", scissors: "Scissor"}
rules = { rock: scissors, paper: rock, scissors: paper }

player_score, computer_score = (0, 0)

def move():
    while True:
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Opps! I didn't understand that. please enter 1,2 or 3")

def result(player, computer):
    global player_score, computer_score, names

    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print('3...')
    print("computer threw: {0}".format(names[computer]) )
    if player == computer:
        print("Tie game")
    else:
        if rules[player] == computer:
            print("Your victory has been assured.")
            player_score += 1
        else:
            print("The computer laughs as you realize you have been defeated")
            computer_score += 1

def play_again():
    answer = input("Would you like toplay again? y/n: ")
    if str(answer).upper() in ('Y','YES','OF COURSE!','OF COURSE'):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def start():
    print("Let's play a game of Rock, Paper, Scissors.")

    while game():
        pass
    scores()

if __name__ == '__main__':
    start()