from Cards import Cards
import random

class Deck():

    def __init__(self):
        self.cards = []
        self.create_deck_of_cards()

    def create_deck_of_cards(self):
        for i in range(10, 0, -1):
            self.cards.append(Cards(i, 4))

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def define_vira(self, deck):
        # print("antes: "+ str(self.cards[0].quantity)) # Debbug do vira antes
        self.vira = deck.remove_card() # o topo do deck se torna vira
        # print("depois: "+ str(self.cards[0].quantity)) # Debbug do vira depois

    def remove_card(self):
        # Percorre todo o deck de cartas
        self.shuffle_deck() # embaralha novamente
        for pos in range(10):
            if self.cards[pos].quantity > 0: # se a carta de valor x tiver acabado, checa a seguinte do baralho
                return self.cards[pos] # retorna a carta no topo

    def define_manilha(self):
        if self.vira.weight == 10:
            return 1
        else:
            return self.vira.weight + 1
    
    def define_manilhas(self, manilha):
        for i in self.cards:
            x = i.return_weight()
            if x == manilha:
                self.manilhas = i
