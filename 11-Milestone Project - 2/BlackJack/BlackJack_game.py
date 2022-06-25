#2nd Milestone Project - BlackJack
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

# CLASS TO CREATE A DECK OF CARDS AND SHUFFLE THEM
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


# CLASS TO CREATE A DECK OF CARDS AND SHUFFLE THEM. ALSO EXTRACT FROM DECK IF NEEDED
class Deck:

    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# CLASS THAT HANDLES/CALCULATES HANDS
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        pass
    
    def adjust_for_ace(self):
        pass


# CLASS THAT HANDLES PLAYER NAME
class Player:
    
    def __init__(self):
        pass

    # GET PLAYER NAME
    def player_name(self):
        self.name = ''
        
        while self.name == '':
            self.name = input('How should I call you?: ')
            if self.name == '':
                print('Please enter a valid name.')
        
        return self.name


# CLASS THAT HANDLES PLAYERS BALANCE/CHIPS 
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        pass
    
    def lose_bet(self):
        pass
    
    #CASH IN
    def get_chips(self):
        self.balance = 0
        
        while self.balance <= 0:
            self.balance = int(input('How much would you like to deposit?: '))
            if self.balance <= 0:
                print('Please enter a valid number (greater than 0).')
        
        return self.balance

    # CASH OUT
    def sell_chips(self, balance):
        pass


# FUNCTIONS

# FUNCTION TO HANDLE IF PLAYER WANTS TO CONTINUE PLAYING
def continue_playing():
    continue_playing = ''

    while continue_playing == '':
        continue_playing = input('\nDo you want to continue playing? (Y = Yes | N = No): ').upper()
        
        if continue_playing == '' and continue_playing == 'Y' and continue_playing == 'N':
            print('Please enter a valid option: Y/N.')

    if continue_playing == 'Y':
        return True
    else:
        return False

def take_bet(balance):
    bet = 0
    
    while bet <= 0:
        bet = int(input("How much would you like to bet?: "))
        if bet <= 0:
            print(f'Please insert a number greater than 0. Your current balance is: ${balance}')
        elif bet > balance:
            print(f"You don't have enough balance. Your current balance is: ${balance}")
    
    return bet


# WELCOME MESSAGE            
print("========| WELCOME TO BLACKJACK!! |========")
player_name = Player()
player_name = player_name.player_name()
print(f"Thank you {player_name}, let's begin!\n")


# GAME LOGIC
while playing == True:
    new_deck = Deck()
    new_deck.shuffle()
    balance = Chips()
    balance = balance.get_chips()

    while balance >= 0 and playing == True:
        print(f"{player_name}, your current chip balance is: ${balance}\n")
        bet = take_bet(balance)
        balance -= bet

        # Deal 2 cards to player and 2 to dealer, show only one of the dealer
        player_hand = []
        player_hand.append(new_deck.deal_one())
        player_hand.append(new_deck.deal_one())
        dealer_hand = []
        dealer_hand.append(new_deck.deal_one())
        dealer_hand.append(new_deck.deal_one())

        # SHOW CARDS
        print('\nHERE ARE THE CARDS ON THE TABLE')      
        print(f"Player's Cards")
        print(player_hand[0] + " and " + player_hand[1])

        playing = continue_playing()


        

    