import random

import colorama
from colorama import Fore, Style


def rounds():
    number = int(input("Number of Rounds you wanna play Rock-Paper-Scissors: "))
    record_list= []

    for i in range(number):
        record_list.append(play())
        print (record_list[i])
    
    print (record_list)
    if (record_list.count('Win') >> record_list.count('Loss')):
        print (Fore.GREEN +"Yay! You Won against Computer!")

    elif (record_list.count('Win') == record_list.count('Loss')):
        print (Fore.BLUE +"Tight! You tie against Computer!")

    else:
        print (Fore.RED +"Oh no! You Lost against Computer!")

def play():
    
    user = user_input()
    computer = random.choice(['s','p','r'])
               
    if (user == computer):
        return 'Tie'
    
    if win_is(user,computer):
    #if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return 'Win'

    return 'Loss'

# r>s, s>p, p>r
def win_is(user,computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

def user_input():
    player = input("what's your choice? \n 'r' for Rock, 'p' for paper, 's' for scissor \n")
    if (player =='r' or player == 'p' or player == 's'):
        return player
    else:
        player = input("Invalid character, Please choose again! \n 'r' for Rock, 'p' for paper, 's' for scissor \n ")
        return player
    # while player !='r' or player != 'p' or player != 's':
    #     player = input("!INVALID CHOICE! please choose again \n 'r' for Rock, 'p' for paper, 's' for scissor \n")
    #     return player

rounds()


