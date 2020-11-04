import random
from functions import multiple_draw, get_coeff

# const
HAND_NB = 5
deck = [
    '2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h', 'J-h', 'Q-h', 'K-h', 'A-h',
    '2-d', '3-d', '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d', 'J-d', 'Q-d', 'K-d', 'A-d',
    '2-c', '3-c', '4-c', '5-c', '6-c', '7-c', '8-c', '9-c', '10-c', 'J-c', 'Q-c', 'K-c', 'A-c',
    '2-s', '3-s', '4-s', '5-s', '6-s', '7-s', '8-s', '9-s', '10-s', 'J-s', 'Q-s', 'K-s', 'A-s'
]


# functions
def ask_boolean(question: str):
    while True:
        response = input(question + ' Oui ou Non.\n').lower()
        if response == 'non' or response == 'n':
            return False
        if response == 'oui' or response == 'o':
            return True


def card_choice(hand: list):
    next_hand = []
    for card in hand:
        if(ask_boolean(f'Conserver la carte : {card} ?')):
            next_hand.append(card)
    return next_hand


def drawer(deck: list):
    hand, deck = multiple_draw(deck, cards=[])
    print('Premier tirage : ', hand)
    hand = card_choice(hand)
    hand, deck = multiple_draw(deck, HAND_NB - len(hand), hand)
    print('Tirage final : ', hand)
    return hand


def party(bankroll: int):
    bet = int(input("Mise en € : "))
    while 0 > bet > bankroll:
        bet = int(input("La mise doit être inférieure a la cagnotte : "))
    hand = drawer(deck)
    coeff, text = get_coeff(hand)
    print(text)
    if coeff > 1:
        print(f'Vous avez gagnez {bet * coeff}€')
    bankroll = bankroll - bet + bet * coeff
    print(f'Votre cagnotte est de {bankroll}€')
    return bankroll


bankroll = int(input("Cagnotte en € : "))
playing = True
print(f'Votre cagnotte est de {bankroll}€')
while playing and bankroll > 0:
    party(bankroll)
    playing = ask_boolean('Continuer à jouer ?')
