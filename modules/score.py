# const
SEQUENCE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def get_card_nb(card: str):
    return card.split('-')[0]


def get_card_color(card: str):
    return card.split('-')[1]


def is_quinte_royal(cards: list):
    return [get_card_nb(card) for card in cards] == ['10', 'J', 'Q', 'K', 'A']


def is_quinte(cards: list):
    for i, card in enumerate(cards[:-1]):
        card_nb = get_card_nb(card)
        next_card_nb = get_card_nb(cards[i + 1])
        if(card_nb == '5' and next_card_nb == 'A'):
            break
        print(next_card_nb)
        print(SEQUENCE[SEQUENCE.index(card_nb)])
        if(next_card_nb != SEQUENCE[
            SEQUENCE.index(card_nb) + 1
        ]):
            return False
    return True


def is_flush(cards: list):
    color = get_card_color(cards[0])
    for card in cards:
        if(get_card_color(card) != color):
            return False
    return True


def count_cards_by_nb(cards: list):
    cards_by_nb = {}
    for card in cards:
        card_nb = get_card_nb(card)
        if card_nb not in cards_by_nb:
            cards_by_nb[card_nb] = 0
        cards_by_nb[card_nb] += 1
    return cards_by_nb


def get_coeff(hand: list):
    # sort hand by SEQUENCE
    hand.sort(key=lambda card: SEQUENCE.index(get_card_nb(card)))

    # cards sequences
    if(is_quinte_royal(hand) and is_flush(hand)):
        return 250, 'Vous avez fait une quinte flush royale !'

    if (is_quinte(hand)):
        if(is_flush(hand)):
            return 50, 'Vous avez fait une quinte flush !'
        return 4, 'Vous avez fait une quinte !'

    if (is_flush(hand)):
        return 6, 'Vous avez fait un flush !'

    # pairs groups
    cards_by_nb = count_cards_by_nb(hand)
    combo = sorted(cards_by_nb.values(), reverse=True)

    if(combo[0] == 4):
        return 25, 'Vous avez fait un carré !'

    if(combo[0] == 3):
        if(combo[1] == 2):
            return 9, 'Vous avez fait un full !'
        return 3, 'Vous avez fait un brelan !'

    if(combo[0] == 2):
        if(combo[1] == 2):
            return 2, 'Vous avez fait une double paire !'
        return 1, 'Vous avez fait une paire. Vous conservez votre mise.'

    return 0, 'Vous avez perdu votre mise.'
