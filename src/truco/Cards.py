import random

class Cards():

    def __init__(self, weight, quantity):
        self.weight = weight
        self.quantity = quantity
        self.naipe = ['PAUS', 'COPAS', 'ESPADAS', 'OUROS']

    def return_weight(self):
        return self.weight

    def return_random_naipe(self):
        random.shuffle(self.naipe)
        return self.naipe.pop()

    def return_number_card(self):
        cards = {
            1: '4',
            2: '5',
            3: '6',
            4: '7',
            5: 'Q',
            6: 'J',
            7: 'K',
            8: 'A',
            9: '2',
            10: '3',
        }
        return cards[self.weight]

