'''
This is a Black Jack Game Representation
'''

########################################################################################################################
# Creating Class of a Card

class Card():
    
    def __init__(self,rank,suit,value):
        
        self.rank = rank
        self.suit = suit
        self.value = value
        
    def __len__(self):
        return int(self.value)
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


########################################################################################################################
# Creating Class of a player

class Player():
    
    def __init__(self, nickname = 'Arczibald the Bald', bankroll = 0, current_bet = 0):
        
        self.nickname = str(nickname)
        self.bankroll = float(bankroll)
        self.current_bet = float(current_bet)
        
    def defining_player(self):

        self.nickname = str(input("What's your nickname? "))
        print(f'{self.nickname}, you are about to play Black Jack!')

        while True:
            try:
                self.bankroll = float( input("How much money would you like to deposite to your account? ") )
                break
                
            except:
                print('Sorry, this is not money. Please provide a real amount.')
                continue
                
        print(f'Welcome to the game, {self.nickname}. Deposit done! Thank you.')

    def deposit(self):
            
        money_deposit = 0
        choice = ''

        while True:
             
            print(f'Your bankroll equals to {self.bankroll}.', end =' ')
            choice = input('Do you wish to deposit money to your account? Y / N: ')

            if choice.lower() not in ['y','n']:
            	clear_output()
            	print("Sorry, wrong input.")
            	continue

            else:
            	break

        while self.bankroll	== 0 or choice == 'y':
            
            if self.bankroll == 0:
                print('You bankroll equals to 0. You need to have money in order to play.')

            while True:

                try:
                    while True:

                        money_deposit = float( input("How much money would you like to deposite to your account? ") )

                        if money_deposit < 0:
                            clear_output()
                            print("Sorry. It can't be lower than 0")
                            continue

                        else:
                            self.bankroll = self.bankroll + money_deposit
                            print(f'{self.nickname}, deposit is done! Thank you.')
                            choice = 'n'
                            break
                    break

                except:
                    print('Sorry, this is not money. Please provide a real amount.')
                    continue

    def bet(self):
        
        while True:
            
            while True:
                
                try:
                    self.current_bet = float(input("How much money do you wanna bet? "))
                    break
                    
                except:
                    print('Sorry, this is not money. Please provide a real amount.')
                    continue

            if self.current_bet > self.bankroll:
                print("Sorry, you don't have that much money.")
                continue
                      
            else:
                if self.current_bet == self.bankroll:
                    print('\n\nAll in, huh? Good Luck!\n\n')
                elif self.current_bet > 0.5 * self.bankroll:
                    print('\n\nWoow. Playing Hard. I like that. Crossing fingers for your win!\n\n')
                elif self.current_bet < 0.1 * self.bankroll:
                    print('\n\nBet done. We have got a cheaposaurus right there.\n\n')
                else:
                    pass
                break
        
    def win_loose(self, won_or_lost):
        if won_or_lost == True:
            self.bankroll = self.bankroll + self.current_bet
        else:
            self.bankroll = self.bankroll - self.current_bet
            
        self.current_bet = 0

########################################################################################################################
# Drawing random card from the deck in Card() Class
# Poping it out of a remaining deck of cards
# Appending it to Drawer's Deck (Player or dealer)

import random

def random_card(drawers_deck):

    drawn_card = random.choice(list(deck_of_cards.keys()))
    drawers_deck.append(deck_of_cards[drawn_card])
    deck_of_cards.pop(drawn_card)
    
    return drawers_deck

########################################################################################################################
# Printing drawn of cards after players turn

def deck_print_shown(deck):
    
    print(" ,----------," *len(deck))
    print(f" |{'':^10}|" *len(deck))
    
    for card in deck:
        print(f" |{card.rank:^10}|", end = '')
    
    print('')
    print(f" |{'of':^10}|" *len(deck))
    
    for card in deck:
        print(f" |{card.suit:^10}|", end = '')
    
    print('')
    print(f" |{'':^10}|" *len(deck))
    print(f" '----------'" *len(deck))

########################################################################################################################
# Printing dealers cards - first hidden and second shown

def deck_print_first_hidden(deck):
    
    print(" ,----------," *len(deck))
    print(f" |{'':^10}|" *len(deck))
    
    print(f" |{'':^10}|", end = '')
    print(f" |{deck[1].rank:^10}|", end = '')
    
    print('')
    print(f" |{'':^10}|", end = '')
    print(f" |{'of':^10}|")
    
    print(f" |{'':^10}|", end = '')
    print(f" |{deck[1].suit:^10}|", end = '')
    
    print('')
    print(f" |{'':^10}|" *len(deck))
    print(f" '----------'" *len(deck))

########################################################################################################################
# Printing game table

def print_game_table(players_cards, dealers_cards):    
    
    if hit_or_stay == True:
        deck_print_first_hidden(dealers_cards)
    else:
        deck_print_shown(dealers_cards)
    print(f'{" DEALER`S CARDS"}')
    print('\n\n\n\n\n\n')
    print('             ' * (len(players_cards) - 2), end = '')
    print(f'{human_player.nickname.upper()+"`S CARDS" :>26}')
    deck_print_shown(players_cards)

########################################################################################################################
# Calculating and returning deck value
# Includes secanrios with Ace being 1 or 11

def deck_value(deck):
    
    deck_value = 0
    ace_count = 0
    
    for card in deck:
        deck_value = deck_value + card.value
        if card.rank == 'Ace':
            ace_count+=1
    
    while ace_count != 0 and deck_value > 21:
        deck_value = deck_value - 10
        ace_count -= 1
        
    return deck_value

########################################################################################################################
# Asks players if he wants to draw another card
# Returns False if no, returns true if yes

def hit_or_stay_func():
    
    choice = ''
    posibilities = ['y', 'n']
    
    while choice.lower() not in posibilities:
        
        choice = input('Do you wish to draw another card? Y / N: ')
        clear_output()
        
        if choice.lower() not in posibilities:
            print('Wrong input!')
            continue
        else:
            break
    
    if  choice.lower() == 'y':
            
        print('HIT ME!')
        return True
        
    elif choice.lower() == 'n':
            
        print('Stay.')
        return False

########################################################################################################################
# Checking if deck value is bigger than 21 or lower than 21

def if_not_busted(deck_value):
    
    if deck_value > 21:
        print('BUSTED!')
        return False
    else:
        return True

########################################################################################################################
# Cleaning screen

def clean_console():
        clear = lambda: os.system('cls')
        clear()

#########################################################################################
#Checking if player is ready to play

#def are_you_ready():
#
#    xyz=''
#
#    while xyz.lower() not in ['y','"y"']:
#        
#        if xyz.lower() not in ['y','"y"']:
#            xyz=input('Type "Y" when ready to play: ')
#            clear_output()
#
#        if xyz.lower() not in ['y','"y"']:
#            print(f'{human_player.nickname}, do you need few more minutes?')


#########################################################################################
#Checking if player wants to play another game

def wanna_play_check():
    xyz=''
    while xyz.lower() not in ['y','n']:
        
        if xyz.lower() not in ['y','n']:
            xyz=input('This the end of this round. Do you want to play one more round? Y or N: ')
            clear_output()

        if xyz.lower() not in ['y','n']:
            print('Wrong input.')
        else:
            if xyz.lower()=='y':
                human_player.deposit()
                return True
            else:
                return False


def final_message(if_player_not_busted, if_dealer_not_busted):
    if if_player_not_busted == False:
        print(f"BUSTED!\nYou Lost! Your deck value is {players_deck_value}, dealer's deck value is {dealers_deck_value}.")
        print(f"You lost {human_player.current_bet}.", end = ' ')
        human_player.win_loose(False)
        print(f"Now your bankroll equals to {human_player.bankroll}")

    elif if_dealer_not_busted == False:
        print(f"Dealer busted! Congratulations! You won! Your deck value is {players_deck_value}, dealer's deck value is {dealers_deck_value}.")
        print(f"You won {human_player.current_bet}.", end = ' ')
        human_player.win_loose(True)
        print(f"Now your bankroll equals to {human_player.bankroll}")

    else:
        print(f"You Lost! Your deck value is {players_deck_value}, dealer's deck value is {dealers_deck_value}.")
        print(f"You lost {human_player.current_bet}.", end = ' ')
        human_player.win_loose(False)
        print(f"Now your bankroll equals to {human_player.bankroll}")

########################################################################################################################
########################################################################################################################
########################################################################################################################
# BLACK JACK GAME LOGIC

from IPython.display import clear_output
import os

clean_console()

wanna_play = True

human_player = Player()

human_player.defining_player()

while wanna_play == True:

    ########################################################################################################################
    # Creating representation of a deck of cards
    
    rank_and_value = [('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 10), ('Queen', 10), ('King', 10), ('Ace', 11)]
    french_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck_of_cards = {}
    
    for rank in rank_and_value:
        
        for suit in french_suit:
            deck_of_cards[(str(rank[0]) + ' of ' + str(suit))] =  Card(rank[0], suit, rank[1])
    
    ########################################################################################################################
    # Defining variables
    
    if_player_not_busted = True
    if_dealer_not_busted = True
    hit_or_stay = True
    players_deck = []
    dealers_deck = []

    # asking player how much he wants to bet
    human_player.bet()

    ########################################################################################################################
    # Drawing 2 cards for player and 2 cards for dealer

    random_card(players_deck)
    random_card(dealers_deck)
    random_card(players_deck)
    random_card(dealers_deck)  
    
    # printing game table
    print_game_table(players_deck, dealers_deck)

    # calucuating players deck value
    dealers_deck_value = deck_value(dealers_deck)
    players_deck_value = deck_value(players_deck)
    
    ##############################################################################################
    # starting players move
    # asking player if he wants to play after seeing first two cards
    hit_or_stay = hit_or_stay_func()
    
    while if_player_not_busted == True and hit_or_stay == True:

        # drawing random card
        players_deck = random_card(players_deck)

        # calucuating players deck value
        players_deck_value = deck_value(players_deck)

        # printing game table
        clean_console()

        # checking if not busted (deck value >21)
        if_player_not_busted = if_not_busted(players_deck_value)

        # printing game table
        print_game_table(players_deck, dealers_deck)

        # asking player if he wants to HIT or Stay
        if if_player_not_busted == True:
            hit_or_stay = hit_or_stay_func()
        else:
        	hit_or_stay = False

    while if_player_not_busted == True and if_dealer_not_busted == True and dealers_deck_value <= players_deck_value:
        # drawing random card
        dealers_deck = random_card(dealers_deck)
        
        # calucuating players deck value
        dealers_deck_value = deck_value(dealers_deck)

        # checking if not busted (deck value >21)
        if_dealer_not_busted = if_not_busted(dealers_deck_value)

        # cleaning console
        clean_console()

        # printing game table
        print_game_table(players_deck, dealers_deck)


    # printing game table
    clean_console()

    # printing game table
    print_game_table(players_deck, dealers_deck)

    # printing finall message to a player and adjusting his bankroll
    final_message(if_player_not_busted, if_dealer_not_busted)

    # checking if player wants to have another go
    wanna_play = wanna_play_check()

    # clearing console
    clean_console()


print(f'Thanks for playing. You are leaving with {human_player.bankroll}. It was a pleasure.')