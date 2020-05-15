import random
from Deck2 import Deck
from Deck2 import value

player_cards = []
dealer_cards = []

while len(dealer_cards) !=2:
    dealer_cards.append(Deck.pop(0))
    if len(dealer_cards) == 2:
        print("The dealer has X and", dealer_cards[1])

while len(player_cards) !=2:
    player_cards.append(Deck.pop(0))
    if len(dealer_cards) == 2:
        print("You have", player_cards)



