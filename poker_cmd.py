# imports
import random
from modules.draw import HAND_NB, init_deck, multiple_draw
from modules.score import get_coeff


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
    hand = drawer(init_deck())
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
