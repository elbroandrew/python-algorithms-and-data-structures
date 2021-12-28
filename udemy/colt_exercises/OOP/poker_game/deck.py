from udemy.colt_exercises.OOP.poker_game.card import Card


class Deck:
    def __init__(self):
        suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)

Deck()