#2nd Milestone Project - BlackJack
from hashlib import new
import os
import random
os.system('cls')

# GLOBAL VARIABLES
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


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

    def deal(self):
        return self.all_cards.pop()


# CLASS THAT HANDLES/CALCULATES HANDS
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# CLASS THAT HANDLES PLAYERS BALANCE/CHIPS 
class Chips:
    
    def __init__(self):
        self.balance = 0 
        self.bet = 0

          
    #CASH IN
    def get_chips(self):      
        while self.balance <= 0:
            self.balance = int(input('How much would you like to deposit?: '))
            if self.balance <= 0:
                print('Please enter a valid number (greater than 0).')
        
        return self.balance

    def take_bet(self):
        
        while self.bet <= 0:
            self.bet = int(input("How much would you like to bet?: "))
            if self.bet <= 0:
                print(f'Please insert a number greater than 0. Your current balance is: ${self.balance}')
            elif self.bet > self.balance:
                print(f"You don't have enough balance. Your current balance is: ${self.balance}")
        
        return self.bet

    def win_bet(self):
        self.balance += self.bet
    
    def lose_bet(self):
        self.balance -= self.bet

    # CASH OUT
    def sell_chips(self, balance):
        pass


# FUNCTIONS

# TAKE BET



# GET PLAYER NAME
def player_name():
    name = ''

    while name == '':
        name = input('How should I call you?: ')
        if name == '':
            print('Please enter a valid name.')
    
    print(f"Thank you {name}, let's begin!\n")

    return name


def show_cards(player_hand, dealer_hand):
    
    print('\nHERE ARE THE CARDS ON THE TABLE')

    print(f"Dealer's Cards")
    print(dealer_hand.cards[1])

    print(f"\nPlayer's Cards")
    for card in player_hand.cards:
        print(card)


def show_all_cards(player_hand, dealer_hand):
    
    print('\nHERE ARE THE CARDS ON THE TABLE')

    print(f"Dealer's Cards")
    for card in dealer_hand.cards:
        print(card)

    print(f"\nPlayer's Cards")
    for card in player_hand.cards:
        print(card)


def hit_or_stand(deck,hand):

    round = True

    while True:
        x = input('\nHit(H) or Stand(S)?: ').upper()

        if x == 'H':
            hit(deck,hand)
        elif x =='S':
            print("Player Stands, Dealer's Turn")
            round = False
        else:
            print('Enter valid option')
            continue
        break
    
    return round

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

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


def game_status(player_hand,dealer_hand,bet):

    if player_hand.value > 21:
        player_busts(player_hand,dealer_hand,bet)
        return False

    if dealer_hand.value > 21:
        dealer_busts(player_hand,dealer_hand,bet)
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_hand,dealer_hand,bet)
    elif dealer_hand.value < player_hand.value:
        player_wins(player_hand,dealer_hand,bet)
    else:
        push(player_hand,dealer_hand,bet)


def player_busts(player_hand,dealer_hand,bet):
    print('BUST PLAYER!')
    bet.lose_bet()

def player_wins(player_hand,dealer_hand,bet):
    print('PLAYER WINS!')
    bet.win_bet()

def dealer_busts(player_hand,dealer_hand,bet):
    print('PLAYER WINS! DEALER BUSTED!')
    bet.win_bet()
    
def dealer_wins(player_hand,dealer_hand,bet):
    print('DEALER WINS!')
    bet.lose_bet()
    
def push(player_hand,dealer_hand,bet):
    print('Dealer and player tie! PUSH!')
    bet.win_bet()


# WELCOME MESSAGE            
print("========| WELCOME TO BLACKJACK!! |========")
player_name = player_name()
balance = Chips()
available_balance = balance.get_chips()
bet = Chips()
playing = True

# GAME LOGIC
while playing == True:
    deck = Deck()
    deck.shuffle()
    round = True 
    
    print(f"{player_name}, your current chip balance is: ${available_balance}\n")
    bet_amount = bet.take_bet()
    print(bet_amount)
    
    # DEAL CARDS
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # SHOW CARDS - FIRST ROUND
    show_cards(player_hand, dealer_hand)
    
    while round:
        # ASK PLAYER FOR NEXT MOVE
        hit_or_stand(deck,player_hand)
        show_cards(player_hand, dealer_hand)

        # CHECK IF PLAYER IS ABOVE 21
        round = game_status(player_hand,dealer_hand,bet_amount)
    
    # DEALER'S TURN
    while dealer_hand.value < 17:
        hit(deck,dealer_hand)

    # SHOW ALL CARDS
    show_all_cards(player_hand,dealer_hand)

    # SITUATION ANALYSIS #2
    game_status(player_hand,dealer_hand,bet_amount)

    playing = continue_playing()

    if playing != True:
        print('Thank you for playing! bye!')
        break