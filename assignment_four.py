# Eva D.
# date
# description

import random

def get_card():
    card_number = float(random.randint(1,10))
    return card_number


def get_winner(user_total, dealer_total):
    if dealer_total>user_total or dealer_total==user_total:
        return "The dealer wins!"
    else:
        return "You win!"

def main():
    user_card_1 = float(get_card())
    user_card_2 = float(get_card())
    user_total = user_card_1+user_card_2
    print("You drew a "+str(user_card_1)+" and a "+str(user_card_2)+". Your current total is "+str(user_total))
    draw_another = input("Would you like to draw another card (Y or N)? ")
    while draw_another == "Y":
        new_card = float(get_card())
        user_total = user_total + new_card
        print("You drew a "+str(new_card)+". Your total is now "+str(user_total))
        if float(user_total) >= 21:
            break
        else:
            draw_another = input("Would you like to draw another card (Y or N)? ")
    if user_total>21:
        print("Looks like you went over 21... You lose!")
    else:
        dealer_card_1 = get_card()
        dealer_card_2 = get_card()
        dealer_total = dealer_card_1+dealer_card_2
        print("The dealer drew a "+str(dealer_card_1)+" and a "+str(dealer_card_2)+
              ", which makes a total of "+str(dealer_total))
        print(get_winner(user_total, dealer_total))



main()




