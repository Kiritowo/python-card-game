from DeckShuffle import deck

def score(cards):
    count = 0
    aceCount = 0

    for i in cards:
        if (i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or  i[1] == 'K'):
            count += 10


def createCards(myDeck):
    card1 = []
    card2 = []
    card1.append(myDeck.pop())
    card2.append(myDeck.pop())
    print (card1)
