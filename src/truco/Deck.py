from Cards import Cards
import random

class Deck():

    def __init__(self):
        self.cards = []
        self.create_deck_of_cards()

    def create_deck_of_cards(self):
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

        self.cards.append(ZAP);
        self.cards.append(DAMA);
        self.cards.append(SETE_COPAS);
        self.cards.append(VALETE);
        self.cards.append(ESPADILHA);
        self.cards.append(REI);
        self.cards.append(SETE_OUROS);
        self.cards.append(AS);
        self.cards.append(TRES);
        self.cards.append(DOIS);

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def define_vira(self, deck):
        # print("antes: "+ str(self.cards[0].quantity)) # Debbug do vira antes
        self.vira = deck.remove_card() # o topo do deck vira manilha
        # print("depois: "+ str(self.cards[0].quantity)) # Debbug do vira depois

    def remove_card(self):
        self.cards[0].quantity -= 1
        return self.cards[0] # retorna a carta no topo

    def define_manilha(self):
        if self.vira.weight == 7:
            return 11
        elif self.vira.weight == 13:
            return 1
        else:
            return self.vira.weight + 1