#2nd Milestone Project - BlackJack - This .PY file is following the teacher's code
from hashlib import new
import os
import random
os.system('cls')

# Global variables provided by the course
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):     
        self.deck = []

        for suit in suits:
            for rank in ranks:
                # Create card object
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card) # from Deck.deal() --> single Card(suit,rank)
        self.value += values[card.rank]

        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How much would you like to bet?: '))
        except ValueError:
            print("Please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"You don't have enough chips!. Your current balance is: ${chips.total}")
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('\nHit(H) or Stand(S)?: ').upper()

        if x == 'H':
            hit(deck,hand)
        elif x =='S':
            print("Player Stands, Dealer's Turn")
            playing = False
        else:
            print('Enter valid option')
            continue
        break


def show_some(player,dealer):

    # Show only one card of the dealer's
    print(f"\nDealer's Hand:")
    print("First Card hidden")
    print(dealer.cards[1])

    # Show 2 cards, player's hand
    print(f"\nPlayer's Hand:")
    for card in player.cards:
        print(card)

    #print("\nPlayer's Hand",*players.cards,sep='\n')


def show_all(player,dealer):
    print(f"\Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")

    print(f"\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player,dealer,chips):
    print('BUST PLAYER!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! PUSH!')



while True:
    print('WELCOME TO BLACKJACK')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
           player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand, dealer_hand)


    print('\nPlayer total chips are at: {}'.format(player_chips.total))

    new_game = input('\nDo you want to continue playing? (Y = Yes | N = No): ').upper()

    if new_game == 'Y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break