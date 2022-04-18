from mesa import Agent

class PlayerAgent(Agent):
  def __init__(self, unique_id, model, deck):
    super().__init__(unique_id, model)
    self.name = str("Player "+ str(unique_id))
    self.deck = deck
    self.mao = []

  def set_hand(self):
    for i in range(3):
      card = self.deck.remove_card()
      naipe = card.return_random_naipe()
      number_card = card.return_number_card()
      self.mao.append([number_card, naipe])

    print("mao :") # Imprimindo mao para debug
    for i in range(3):
      print(self.mao[i])


  def step(self):
    print("Ola, eu sou o agente "+ self.name) 
    self.set_hand()