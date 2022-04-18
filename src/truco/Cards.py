import random

def return_card_name(weight):
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
    return cards[weight]

class Cards():
    def __init__(self, weight, quantity):
        self.weight = weight
        self.quantity = quantity
        self.naipe = ['PAUS', 'COPAS', 'ESPADAS', 'OUROS']
        self.name = return_card_name(weight)

    def return_weight(self):
        return self.weight

    def set_weight(self, n):
        self.weight = n

    def return_random_naipe(self):
        random.shuffle(self.naipe)
        self.quantity -= 1
        return self.naipe.pop()

