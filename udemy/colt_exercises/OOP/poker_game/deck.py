from udemy.colt_exercises.OOP.poker_game.card import Card
from random import shuffle


class Deck:
    def __init__(self):
        suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    # custom iterator
    def __iter__(self):
        return iter(self.cards)
    # OR with generator below:
    '''
    def __iter__(self):
        for card in self.cards:
            yield card
    '''

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)
        return self




d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)



