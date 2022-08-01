import random


def play():
    user = input("what's your choice? \n 'r' for Rock, 'p' for paper, 's' for scissor \n")
    if (user =='r' or user == 'p' or user == 's'):
        computer = random.choice(['s','p','r'])
    else:
        return "Invalid Choice!r"
            
    if (user == computer):
        return "Its a Tie :|"
    
    if win_is(user,computer):
        return "You Won!"
    
    return "You Lost!"

# r>s, s>p, p>r
def win_is(user,computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

print (play())
#play()

rounds = input("Number of Rounds you wanna play Rock-Paper-Scissors: ")
