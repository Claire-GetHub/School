import random

#creates a dict, the deck
    #*card* of *suit*: card value
def createCards():
    deck = {}
    #card: card value
    cards = {'ace': 11,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'jack': 10, 'queen': 10, 'king': 10}
    #all suits
    suits = ["hearts", "spades", "clovers", "diamonds"]
    #makes each suit
    for suit in suits:
        #with one of each card
        for card in cards:
            #creates card with formate
            deck[f"{card} of {suit}"] = cards[card]
    return deck



def main ():
    #creates the deck
    deck = createCards()
    p1Hand = {}
    p2Hand = {}
    #player1 goes first
    player1 = True
    winner = None

    while True:
        #if its player1s turn hand is player1s hand otherwise its player2s hand
        hand = p1Hand if player1 else p2Hand
        
        #get a random card
        cardName = random.choice(list(deck.keys()))
        card = (cardName, deck.pop(cardName))

        #if its ace check if we need to chage it from 11 to 1
        if card[1] == 11:
            if sum(hand.values()) + 11 >  21:
                card = (card[0], 1)
                
        #add the card to the players hand
        hand[card[0]] = card[1]

        if sum(hand.values()) >  21:
            winner = "player 2" if player1 else "player 1"
            break
        #change to other player. toggle
        player1 = not player1
    #p1s hand
    print(p1Hand)
    #p2s hand
    print(p2Hand)

    #the winner
    print(winner)

if __name__ == "__main__":
    main()
