# Eva D.
# date
# description

import random

def get_card():
    '''
    Chooses a random number from 1-10 to represent a card randomly drawn.
    :return: the number that was chosen representing a card number (float)
    '''
    card_number = float(random.randint(1,10))
    return card_number


def get_winner(user_total, dealer_total):
    """
    determines the winner by using a boolean logic statement to see if the user had more, less, or equal points to
    the computer (does not have to check if user went over 21, because that has already been done.
    :param user_total: the total points the user amassed at the end of the game (float)
    :param dealer_total: the total points the dealer amassed after drawing two cards (float)
    :return: text stating whether the user wins based on the result of the if and else statements (string)
    """
    if dealer_total>user_total or dealer_total==user_total:
        return "The dealer wins!"
    else:
        return "You win!"

def main():
    # assigns variables to user's first two cards so that program can inform user what cards they drew
    user_card_1 = float(get_card())
    user_card_2 = float(get_card())
    user_total = user_card_1+user_card_2
    print("You drew a "+str(user_card_1)+" and a "+str(user_card_2)+". Your current total is "+str(user_total))
    draw_another = input("Would you like to draw another card (Y or N)? ")
    # while loop allowing user to draw more cards if desired, unless they go over 21 or say no to more cards
    # in which the loop ends
    while draw_another == "Y":
        new_card = float(get_card())
        user_total = user_total + new_card
        print("You drew a "+str(new_card)+". Your total is now "+str(user_total))
        if float(user_total) >= 21:
            break
        else:
            draw_another = input("Would you like to draw another card (Y or N)? ")
   # check for after loop ends to see if the user drew too many cards, either reaching 21 and unable to draw more
    # or by surpassing 21 which would be an automatic loss
    if user_total>21:
        print("Looks like you went over 21... You lose!")
   # if the user didn't reach 21, this has the dealer draw 2 cards, informs the user on what the dealer drew,
    # and then delivers the verdict on who won by calling the get_winner function
    else:
        dealer_card_1 = get_card()
        dealer_card_2 = get_card()
        dealer_total = dealer_card_1+dealer_card_2
        print("The dealer drew a "+str(dealer_card_1)+" and a "+str(dealer_card_2)+
              ", which makes a total of "+str(dealer_total))
        print(get_winner(user_total, dealer_total))



main()




