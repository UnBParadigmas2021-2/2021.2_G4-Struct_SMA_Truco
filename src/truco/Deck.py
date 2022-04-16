from .Cards import Cards

class Deck():

    def __init__(self):
        self.cards = create_deck_of_cards()

    def create_deck_of_cards():
        ZAP = Cards(11, 1)
        SETE_COPAS = Cards(10, 1)
        ESPADILHA = Cards(9, 1)
        SETE_OUROS = Cards(8, 1)
        TRES = Cards(7, 4)
        DOIS = Cards(6, 4)
        AS = Cards(5, 3)
        REI = Cards(4, 4)
        VALETE = Cards(3, 4)
        DAMA = Cards(2, 4)
