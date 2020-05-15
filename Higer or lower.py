from random import shuffle
#Definition used to create deck and then shuffle it
def deck():
    deck = []
    for suit in ['H','S','D','C']:
        for rank in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
            deck.append(suit+rank)
    shuffle(deck)

    return deck
#Definition gives value to the cards
def score(cards):
    count = 0

    for i in cards:
        if (i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or  i[1] == 'K'):
            count += 10
        #Value of ace changes on scenario
        elif (i[1] == 'A') and game == 'L':
            count += 1
        elif (i[1] == 'A') and game == 'H':
            count += 11
        #Sets value of cards to their rank    
        elif(i[1] != 'A'):
            count += int(i[1])

    return count

#Creates two arrays, one for card player sees and one for guess. Also pops two cards from the array
def createCards(myDeck):
    card1 = []
    card2 = []
    card1.append(myDeck.pop())
    card2.append(myDeck.pop())

    return [card1, card2]


game = ""
myDeck = deck()
hands = createCards(myDeck)
dealer = hands[0]
player = hands[1]

#Sets the conditions for the game to run and end
while True:
    #Imports the value for each card
    dealerCount = score(dealer)
    playerCount = score(player)
    print("The current card is ")
    print(player)

    #Determines if the game ends or continues depending on circumstance
    game = input("H: Higher or L: lower?\n")
    if game == "H" and dealerCount > playerCount:
        print("Correct")
    if game == "L" and playerCount > dealerCount:
        print("Correct")
    if game == "H" and dealerCount < playerCount:
        print("Incorrect")
        print(dealer)
        break
    if game == "L" and playerCount < dealerCount:
        print("Incorrect")
        print(dealer)
        break
    if game == "L" and playerCount == dealerCount:
        print("Even")
    if game == "H" and playerCount == dealerCount:
        print("Even")
    #Sets the guessed card to be the new card being presented
    player = dealer


