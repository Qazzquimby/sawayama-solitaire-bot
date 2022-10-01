import dataclasses
import random

"""Sawayama solitaire(zachtronics) implementation + bot"""


@dataclasses.dataclass
class Suit:
    name: str
    color: str
    symbol: str

    def __str__(self):
        return self.name


SUITS = [
    Suit("Hearts", "red", "♥"),
    Suit("Diamonds", "red", "♦"),
    Suit("Spades", "black", "♠"),
    Suit("Clubs", "black", "♣"),
]


@dataclasses.dataclass
class Card:
    suit: Suit
    value: int

    def __str__(self):
        return f"{self.suit.symbol}{self.value}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Pile:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def __str__(self):
        return " ".join(str(card) for card in self.cards)


class Game:
    NUM_PILES = 7

    def __init__(self):
        self.deck = Deck()
        self.stack_piles = [Pile() for _ in range(self.NUM_PILES)]
        self.completion_piles = [Pile() for _ in range(len(SUITS))]
        self.deck_space = None
        self._initial_deal()

    def _initial_deal(self):
        for i, stack_pile in enumerate(self.stack_piles):
            for _ in range(i + 1):
                stack_pile.add_cards([self.deck.draw()])

    def has_won(self):
        return all(len(pile.cards) == 13 for pile in self.completion_piles)
