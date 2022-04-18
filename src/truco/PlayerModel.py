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
    self.play = []
    self.pairs_points = [0, 0]
    self.partial_pair_points = [0, 0]
    self.deck = deck

    for i in range(self.num_agents):
      # player_name = str(input("Nome do Jogador " + str(i+1) + " : "))
      names = ['a','b','c','d']
      player_name = names[i]
      a = PlayerAgent(i, self, player_name, i%2) # Criando o PlayerAgent
      self.schedule.add(a) # adicionando o agente ao schedule
      self.agents.append(a)

  def step(self): # Usado para debugar o step dos agentes. No momento imprime no console o id do agente
    self.schedule.step()
    print('--------------------------')
    for _ in range(3):
      self.schedule = BaseScheduler(self)
      for j in self.agents:
        self.schedule.add(j)
      self.schedule.step()
      self.step_point()
      self.play = []
      print('--------------------------')
      if self.partial_pair_points[0] == 2:
        print("Dupla 1 ganhou!")
        break
      if self.partial_pair_points[1] == 2:
        print("Dupla 2 ganhou!")
        break


  def step_point(self):
    pair_play = [0,0]
    for play in self.play:
      pair_play[play['pair']] = max(pair_play[play['pair']], play['play'][2])
    if pair_play[0] > pair_play[1]:
      print("Ponto da dupla 1")
      self.partial_pair_points[0] += 1
    elif pair_play[1] > pair_play[0]:
      print("Ponto da dupla 2")
      self.partial_pair_points[1] += 1
    else:
      print("Empate")
