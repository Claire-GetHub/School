import random

def createCards():
    deck = {}
    cards = {'ace': -1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'jack': 10, 'queen': 10, 'king': 10}
    suits = ["hearts", "spades", "clovers", "diamonds"]
    for suit in suits:
        for card in cards:
            deck[f"{card} of {suit}"] = cards[card]
    return deck



def main ():
    deck = createCards()
    p1Hand = {}
    p2Hand = {}
    player1 = True
    winner = None

    while True:
        hand = p1Hand if player1 else p2Hand
        
        cardName = random.choice(list(deck.keys()))
        card = (cardName, deck.pop(cardName))

        if card[1] == -1:
            if sum(hand.values()) + 11 >  21:
                card = (card[0], 1)
            else:
                card = (card[0], 11)

        hand[card[0]] = card[1]

        if sum(hand.values()) >  21:
            winner = "player 2" if player1 else "player 1"
            break

        player1 = not player1
    print(p1Hand)
    print(p2Hand)
    print(winner)

if __name__ == "__main__":
    main()