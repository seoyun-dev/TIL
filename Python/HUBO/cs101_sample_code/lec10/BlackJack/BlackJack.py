import random
from cs1graphics import *

img_path='./BlackJack/'

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', \
              '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

bj_board = Canvas(600,400,'dark green','Black Jack 101')

#===================================================================
# create an empty class
class Card: 
    pass
#===================================================================

def create_deck(number = 1):
    deck = []
    for i in range(number):
        for suit in suit_names:
            count=0
            for face in face_names:
                card = Card()
                card.suit = suit
                card.face = face
                card.value = value[count]
                card.img = Image(img_path+suit+'_'+face+'.png')
                card.state = True
                deck.append(card)
                count=count+1
    random.shuffle(deck)
    return deck

create_deck()


def hand_value(hand):
    sum = 0
    for i in range(len(hand)):
        sum = sum + hand[i].value
    return sum


def card_string(card):
    if card.face=="Ace":
        return 'an ' + card.face + ' of ' + card.suit
    else:
        return 'a ' + card.face + ' of ' + card.suit


def ask_yesno(prompt):
    while True:
        ans = raw_input(prompt)
        if ans=="y":
            return True
        elif ans=="n":
            return False
        else:
            print "I beg your pardon!"

            
def draw_card(dealer,player):
    depth = 100
    x0,y0 = 100,100
    x1,y1 = 100,300

    bj_board.clear()
    
    for i in range(len(dealer)):
        if dealer[i].state:
            dealer[i].img.moveTo(x0, y0)
            depth = depth -5
            dealer[i].img.setDepth(depth)
            bj_board.add(dealer[i].img)
        else:
            hiddencard = Image(img_path+"Back.png")
            depth = depth -5
            hiddencard.setDepth(depth)
            hiddencard.moveTo(x0, y0)
            bj_board.add(hiddencard)
        x0+=50
    
    depth = 100
    for i in range(len(player)):
        player[i].img.moveTo(x1, y1)
        depth = depth -5
        player[i].img.setDepth(depth)
        bj_board.add(player[i].img)
        x1+=50

    return True

#==============================================================
# this is the main function
        
def main():

	# create an empty list
    deck = [] 

    while True:    
        # prompt for starting a new game and create a deck
        print "Welcome to Black Jack 101!\n"
        if len(deck)<12:
            deck = create_deck()
    
    # create two hands of dealer and player
        dealer = []
        player = []

    # initial two dealings
        card = deck.pop()
        print "You are dealt " + card_string(card)
        player.append(card)

        card = deck.pop()
        print "Dealer is dealt a hidden card"
        card.state=False
        dealer.append(card)

        card = deck.pop()
        print "You are dealt " + card_string(card)
        player.append(card)

        card = deck.pop()
        print "Dealer is dealt " + card_string(card)
        dealer.append(card)

        print "Your total is", hand_value(player)
        draw_card(dealer,player)


    # player's turn to draw cards
        while hand_value(player) < 21 \
                and ask_yesno("Would you like another card? (y/n) "):
        # draw a card for the player
            card = deck.pop()
            print "You are dealt " + card_string(card)
            player.append(card)
            print "Your total is", hand_value(player)
        
            draw_card(dealer,player)
    # if the player's score is over 21, the player loses immediately.     
        if hand_value(player) > 21:
            print "You went over 21! You lost."
            dealer[0].state = True
            draw_card(dealer,player)
        else:
        # draw cards for the dealer while the dealer's score is less than 17
            print "\nThe dealer's hidden card was " + card_string(dealer[0])
            while hand_value(dealer) < 17:
                card = deck.pop()
                print "Dealer is dealt " + card_string(card)
                dealer.append(card)
                print "The dealer's total is", hand_value(dealer)
        
            dealer[0].state = True
            draw_card(dealer,player)
        # summary        
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            print "\nYour total is", player_total
            print "The dealer's total is", dealer_total
        
            if dealer_total > 21:
                print "The dealer went over 21! You win!"
            else:
                if player_total > dealer_total:
                    print "You win!"
                elif player_total < dealer_total:
                    print "You lost!"
                else:
                    print "You have a tie!"
            
        if not ask_yesno("\nPlay another round? (y/n) "):
            bj_board.close()
            break

#==============================================================
# executing the main function
main()
