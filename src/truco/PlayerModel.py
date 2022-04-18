from mesa import Model
from PlayerAgent import PlayerAgent
from mesa.time import BaseScheduler

class PlayerModel(Model):
  "Um jogador com nome e deck de cartas"

  def __init__(self, N, deck):
    self.agents = []
    self.num_agents = N
    self.play = []
    self.pairs_points = [0, 0]
    self.partial_pair_points = [0, 0]
    self.deck = deck

  def step(self):
    if not self.agents:
      self.schedule = BaseScheduler(self)
      for i in range(self.num_agents):
        # player_name = str(input("Nome do Jogador " + str(i+1) + " : "))
        names = ['a','b','c','d']
        player_name = names[i]
        a = PlayerAgent(i, self, player_name, i%2)
        self.schedule.add(a)
        self.agents.append(a)
      self.schedule.step()
      print('--------------------------')
    
    self.play_round()

  def step_point(self):
    pair_play = [self.get_winning_play(self.play[0], self.play[2]), self.get_winning_play(self.play[1], self.play[3])]
    best_play = self.get_winning_play(pair_play[0], pair_play[1])
    self.partial_pair_points[best_play['pair']] += 1
    print("Ponto da dupla", best_play['pair'] + 1)

  def play_round(self):
    for _ in range(3):
      self.schedule = BaseScheduler(self)
      for agent in self.agents:
        self.schedule.add(agent)
      self.schedule.step()
      self.step_point()
      self.play = []
      print('--------------------------')
      if self.has_partial_winner():
        break

  def has_partial_winner(self):
    if self.partial_pair_points[0] == 2:
      print("Dupla 1 ganhou!")
      return True
    if self.partial_pair_points[1] == 2:
      print("Dupla 2 ganhou!")
      return True
    return False

  def get_winning_play(self, a, b):
    if a['play'][2] > b['play'][2]:
      return a
    if a['play'][2] < b['play'][2]:
      return b
    nipes_order = ['OUROS', 'ESPADAS', 'COPAS', 'PAUS']
    if nipes_order.index(a['play'][1]) > nipes_order.index(b['play'][1]):
      return a
    else:
      return b