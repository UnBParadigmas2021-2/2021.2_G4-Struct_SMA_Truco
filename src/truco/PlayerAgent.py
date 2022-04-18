from mesa import Agent

class PlayerAgent(Agent):
  def __init__(self, unique_id, model, name, pair):
    super().__init__(unique_id, model)
    self.name = name
    self.pair = pair
    self.mao = []

  def set_hand(self):
    for i in range(3):
      card = self.model.deck.remove_card()
      naipe = card.return_random_naipe()
      number_card = card.return_number_card()
      self.mao.append([number_card, naipe, card.weight])

  def step(self):
    if not self.mao:
      self.set_hand()
      print("Ola, eu sou o agente", self.name, "e essas são minhas cartas:")
      for i in range(3):
        print(self.mao[i][0], "de", self.mao[i][1])
      return
    play = self.mao.pop()
    print(self.name, "joga", play[0], "de", play[1])
    self.model.play.append({'pair': self.pair, 'play': play})
