import random


class Deck:
    def __init__(self):
        self.suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    def card_set(self):
        mycardset = []
        for n in self.suites:
            for c in self.values:
                mycardset.append((c)+" "+"of"+" "+n)
        return mycardset


    def shuffle(self):
        cards=self.card_set()
        if len(cards) < 52:
            print("cannot shuffle the cards")
        else:
            random.shuffle(self.mycardset)
            return self.mycardset


if __name__ == "__main__":

    objDeck = Deck()

    # to print player 1 cards
    player1Cards = objDeck.card_set
    print('\n Player 1 Cards: \n', player1Cards)
    objShuffleCards = ShuffleCards()
    # to print player 2 Cards
    player2Cards = objShuffleCards.shuffle()
    print('\n Player 2 Cards: \n', player2Cards)
