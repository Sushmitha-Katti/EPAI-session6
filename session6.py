vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
def create_deck_cards_single_expression():
    '''
    This function creates 52 cards in a deck with the help of lambda, map
    input : nothing
    output : list of tuples, where there is all 52 cards combination.

    '''
    cards = []
    list(map(lambda x: list(map(lambda y: cards.append((x,y)), suits)),vals))
    return cards

def create_deck_cards_normal_function():
    '''
    This function creates 52 cards in a deck with the normal function without using zip,lambda,zip
    input : nothing
    output : list of tuples, where there is all 52 cards combination.

    '''
    cards = []

    for val in vals:
        for suit in suits:
            cards.append((val, suit))
    return cards

