# Eva D
# 10/23/2023
# Rock Paper Scissors Game

import random

def tell_user(computer):
    if computer==1:
        return "The computer chose rock.."
    elif computer==2:
        return "The computer chose paper.."
    else:
        return "The computer chose scissors.."

def who_wins(user, computer):
    # 1 is rock, 2 is paper, 3 is scissors
    if user==1 and computer==3:
        return "You win!"
    elif user==2 and computer == 1:
        return "You win!"
    elif  user==3 and computer==2:
        return "You win!"
    elif user == computer:
        return "Looks like it's a tie."
    else:
        return "The computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rock, paper, scissors, shoot!")
    user = float(input("Enter 1 to choose rock, 2 to choose paper, or 3 to choose scissors: "))
    computer = float(random.randint(1,3))
    print(tell_user(computer))
    print(who_wins(user,computer))

if __name__ == '__main__':
    main()