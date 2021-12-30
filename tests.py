from udemy.colt_exercises.OOP.poker_game.card import Card
from udemy.colt_exercises.OOP.poker_game.deck import Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card("A", "Spades")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Spades")
        self.assertEqual(self.card.value, "A")


class DeckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()

    def test_init(self):
        """deck should have a cards attribute, which is a list"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_sufficient_cards(self):
        """_deal should deal the number of card, specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)


if __name__ == '__main__':
    unittest.main()
