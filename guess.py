# eva D
# October 22 2023
# programs a simple guessing game
import random
def generate_number():
    number = float(random.randint(1,10))
    return number

def get_input():
    user_guess = float(input("Guess what number I am thinking of from 1-10! "))
    return user_guess

def how_far(number, user_guess):
    if user_guess>number:
        distance = user_guess - number
        return distance
    elif user_guess<number:
        distance = number-user_guess
        return distance
    else:
        distance = "not needed"
        return distance

def do_response(number, user_guess, distance):
    if user_guess == number:
        print("Congratulations! You're right, I was thinking of "+str(number)+".")
    elif user_guess != number:
        print("Sorry.. my number was "+str(number)+". You were only "+str(distance)+" away!")


def main():
    print("Welcome to the random number game! I just came up with a number, and now you will guess it.")
    number = generate_number()
    user_guess = get_input()
    distance = how_far(number, user_guess)
    do_response(number, user_guess, distance)





main()
