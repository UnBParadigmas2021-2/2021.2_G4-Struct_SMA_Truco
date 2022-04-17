from mesa import Agent

class PlayerAgent(Agent):
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.name = str("Player "+ str(unique_id))

  def step(self):
    print("Ola, eu sou o agente "+ self.name) 