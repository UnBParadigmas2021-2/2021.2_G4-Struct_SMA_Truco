from mesa import Model
from PlayerAgent import PlayerAgent
from mesa.time import BaseScheduler

class PlayerModel(Model):
  "Um jogador com nome e deck de cartas"

  def __init__(self, N, deck):
    # self.nome = nome # Setando o nome do player
    # self.mao = [] # Setando a mao do player
    self.agents = []

    self.schedule = BaseScheduler(self) # instanciando um scheduler para ordenar os steps dos agentes
    self.num_agents = N

    for i in range(self.num_agents):
      # player_name = str(input("Nome do Jogador " + str(i+1) + " : "))
      names = ['a','b','c','d']
      player_name = names[i]
      a = PlayerAgent(i, self, deck, player_name) # Criando o PlayerAgent
      self.schedule.add(a) # adicionando o agente ao schedule
      self.agents.append(a)

  def step(self): # Usado para debugar o step dos agentes. No momento imprime no console o id do agente
    self.schedule.step()
    for _ in range(3):
      self.schedule = BaseScheduler(self)
      for j in self.agents:
        self.schedule.add(j)
      self.schedule.step()
