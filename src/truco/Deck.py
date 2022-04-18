from Cards import Cards
import random

class Deck():

    def __init__(self):
        self.cards = []
        self.create_deck_of_cards()
        self.manilha = 0
        self.vira = 0

    def create_deck_of_cards(self):
        for i in range(10, 0, -1):
            self.cards.append(Cards(i, 4))

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def define_vira(self):
        self.vira = self.remove_card()

    def remove_card(self):
        self.shuffle_deck()
        for pos in range(10):
            if self.cards[pos].quantity > 0:
                return self.cards[pos]

    def define_manilha(self):
        return self.vira.weight % 10 + 1

    def define_manilhas(self):
        self.define_vira()
        manilha = self.define_manilha()
        for i, item in enumerate(self.cards):
            if item.return_weight() == manilha:
                self.cards[i].set_weight(11)
                break

    def get_vira(self):
        return self.vira.name
