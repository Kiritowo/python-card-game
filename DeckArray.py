##import sys
##print(sys.path)

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        #self.score = score
        
    #defines how the card should be displayed
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    #defines the card suits and the range of card values
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for i in [
                    'Ace',
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    'Jack',
                    'Queen',
                    'King'
                    ]:
                self.cards.append(Card(s, i))

    def show(self):
        for c in self.cards:
            c.show()

deck = Deck()
deck.show()
