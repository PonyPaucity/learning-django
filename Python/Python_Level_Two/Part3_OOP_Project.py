#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# from Python.Python_Level_Two.Part3_OOP_Project_SOLUTIONS import SUITE

# Two useful variables for creating Cards.
SUITS = 'Hrt Dia Spa Clb'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.allcards = [(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def deal_hands(self):
        return self.allcards[::2], self.allcards[1::2]

    pass




class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_card(self, added_cards):
        return self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

    pass


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_cards(self):
        drawn_card = self.hand.remove_card()
        print("{} has played {}".format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 1

    pass


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

deck_of_cards = Deck()
deck_of_cards.shuffle()
player_hand1, player_hand2 = deck_of_cards.deal_hands()

terminator = Player("Computer", Hand(player_hand2))
human_name = input("Player Name:")
human = Player(human_name, Hand(player_hand1))

total_round = 0
war_count = 0

while human.still_has_cards() or terminator.still_has_cards():
    total_round += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(human.name+" count: "+str(len(human.hand.cards)))
    print(terminator.name+" count: "+str(len(terminator.hand.cards)))
    print("Both players play a card!")
    print('\n')

    table_cards = []

    computer_played = terminator.play_cards()
    human_played = human.play_cards()

    table_cards.append(computer_played)
    table_cards.append(human_played)

    if computer_played[1] == human_played[1]:
        war_count += 1
        table_cards.extend(terminator.remove_war_cards())
        table_cards.extend(human.remove_war_cards())

        computer_played = terminator.play_cards()
        human_played = human.play_cards()

        if RANKS.index(computer_played[1]) < RANKS.index(human_played[1]):
            print(human.name+" has the higher card, adding to hand.")
            human.hand.add_card(table_cards)
        else:
            print(terminator.name+" has the higher card, adding to hand.")
            terminator.hand.add_card(table_cards)

    else:
        if RANKS.index(computer_played[1]) < RANKS.index(human_played[1]):
            print(human.name+" has the higher card, adding to hand.")
            human.hand.add_card(table_cards)
        else:
            print(terminator.name+" has the higher card, adding to hand.")
            terminator.hand.add_card(table_cards)

print("Great Game, it lasted: "+str(total_round))
print("A war occured "+str(war_count)+" times.")

print('Doesthe computer still ahve card? ')

# Use the 3 classes along with some logic to play a game of war!
