import random

Suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
Ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
Deck = []

value = 1
for Rank in Ranks:
    for Suit in Suits:
        Deck.append((Rank + " of " + Suit, value))
    value = value + 1

random.shuffle(Deck)
