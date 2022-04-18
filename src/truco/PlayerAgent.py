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

  def step(self):
    if not self.mao:
      self.set_hand()
      print("Ola, eu sou o jogador", self.name, "e essas são minhas cartas:")
      cards_list = [self.mao[i][0] + " de " + self.mao[i][1] for i in range(3)]
      print(", ".join(cards_list))
      return

    print('------------------------------- lista de cartas da mao ---------------------------------------')
    print(self.mao)

    max_card = 0
    min_card = 0
    played_card = -1
    for i in range(len(self.mao)):
      
      min_card = min_card if self.mao[i][2] < self.mao[min_card][2] else i
      max_card = max_card if self.mao[i][2] > self.mao[max_card][2] else i

    if not self.model.play:
      played_card = min_card
    else:
      played_card = max_card
      


    print('------------------------------- lista de cartas da mao ---------------------------------------')
    play = {'pair': self.pair, 'play': self.mao[played_card]} #self.mao.pop()
    print(f'play = {played_card}')


    self.mao.pop(played_card)




    #print(self.name, "joga", play[0], "de", play[1], play[2])

    print(f'cartas da mesa = {self.model.play}')
    self.model.play = play
