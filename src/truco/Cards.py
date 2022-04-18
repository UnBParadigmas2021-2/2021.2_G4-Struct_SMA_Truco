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
        if(self.weight == 1):
            return 4
        elif(self.weight == 2):
            return 5
        elif(self.weight == 3):
            return 6
        elif(self.weight == 4):
            return 7
        elif(self.weight == 5):
            return 11
        elif(self.weight == 6):
            return 12 
        elif(self.weight == 7):
            return 13
        elif(self.weight == 8):
            return 1
        elif(self.weight == 9):
            return 2
        elif(self.weight == 10):
            return 3

