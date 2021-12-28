class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


c = Card("A", "Diamonds")
c2 = Card("10", "Spades")
print(c, c2)
