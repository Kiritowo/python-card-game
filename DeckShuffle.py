from random import shuffle

def deck():
    deck = []
    for suit in ['H','S','D','C']:
        for rank in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
            deck.append(suit+rank)

    shuffle(deck)

    return deck

def score(cards):
    count = 0
    aceCount = 0

    for i in cards:
        if (i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or  i[1] == 'K'):
            count += 10
        elif(i[1] != 'A'):
            count += int(i[1])
        else:
            aceCount += 1

    if(aceCount == 1 and count >= 10):
        count += 11
    else:
        count += 1

    return count


def createCards(myDeck):
    card1 = []
    card2 = []
    card1.append(myDeck.pop())
    card1.append(myDeck.pop())
    card2.append(myDeck.pop())
    card2.append(myDeck.pop())

    return [card1, card2]

game = ""
myDeck = deck()
hands = createCards(myDeck)
dealer = hands[0]
player = hands[1]


dealerCount = score(dealer)
playerCount = score(player)

print ("Dealer has :")
print (dealer[1])

print ("You have :")
print (player)
