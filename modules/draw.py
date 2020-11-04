# imports
import random

# const
HAND_NB = 5


def init_deck():
    return [
        '2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h',
        'J-h', 'Q-h', 'K-h', 'A-h',
        '2-d', '3-d', '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d',
        'J-d', 'Q-d', 'K-d', 'A-d',
        '2-c', '3-c', '4-c', '5-c', '6-c', '7-c', '8-c', '9-c', '10-c',
        'J-c', 'Q-c', 'K-c', 'A-c',
        '2-s', '3-s', '4-s', '5-s', '6-s', '7-s', '8-s', '9-s', '10-s',
        'J-s', 'Q-s', 'K-s', 'A-s'
    ]


def draw(deck: list):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck


def multiple_draw(deck: list, nb: int = HAND_NB, cards: list = []):
    for _ in range(nb):
        card, deck = draw(deck)
        cards.append(card)
    return cards, deck
