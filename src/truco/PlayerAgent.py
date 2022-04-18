from mesa import Agent

class PlayerAgent(Agent):
  def __init__(self, unique_id, model, name, pair):
    super().__init__(unique_id, model)
    self.name = name
    self.pair = pair
    self.mao = []

  def set_hand(self):
    for _ in range(3):
      card = self.model.deck.remove_card()
      naipe = card.return_random_naipe()
      number_card = card.name
      self.mao.append([number_card, naipe, card.weight])

  def compare_cards(self, card1, card2):
    naipe = {'PAUS':1, 'COPAS':2, 'ESPADAS':3, 'OUROS':4}
    if (card1[2] > card2[2]):
      return -1
    elif (card1[2] < card2[2]):
      return 1
    else:
      id1 = naipe[card1[1]]
      id2 = naipe[card2[1]]
      if id1 < id2:
        return -1
      return 1

  def step(self):
    if not self.mao:
      self.set_hand()
      print("Ola, eu sou o jogador", self.name, "e essas são minhas cartas:")
      cards_list = [self.mao[i][0] + " de " + self.mao[i][1] for i in range(3)]
      print(", ".join(cards_list))
      return

    max_card = 0
    min_card = 0
    played_card = -1
    for i in range(len(self.mao)):
      
      min_card = min_card if self.mao[i][2] < self.mao[min_card][2] else i
      max_card = max_card if self.mao[i][2] > self.mao[max_card][2] else i

    if self.model.play == {}:
      played_card = min_card
    elif self.compare_cards(self.model.play['play'], self.mao[max_card]) == 1:
      played_card = max_card
    else:
      played_card = min_card
  
    play = {'pair': self.pair, 'play': self.mao[played_card]} 

    self.mao.pop(played_card)

    print(f'Maior carta na mesa = {self.model.play}')
    print(f'Carta a ser jogada = {play}')
    if self.model.play == {} or self.compare_cards(self.model.play['play'], play['play']) == 1:
      self.model.play = play
    print(f'Maior carta na mesa dps de ser atualizada = {self.model.play}')
    
