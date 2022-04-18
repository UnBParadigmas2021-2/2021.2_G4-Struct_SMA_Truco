from mesa import Model
from PlayerAgent import PlayerAgent
from mesa.time import BaseScheduler
from Deck import Deck

class PlayerModel(Model):
  "Um jogador com nome e deck de cartas"

  def __init__(self, N):
    self.agents = []
    self.num_agents = N
    self.play = []
    self.pairs_points = [0, 0]
    self.partial_pair_points = [0, 0]
    self.deck = Deck()

    self.schedule = BaseScheduler(self)
    for i in range(self.num_agents):
      # player_name = str(input("Nome do Jogador " + str(i+1) + " : "))
      names = ['Xandão','Quervinho','Tutu','Quintin']
      player_name = names[i]
      a = PlayerAgent(i, self, player_name, i%2)
      self.schedule.add(a)
      self.agents.append(a)

  def step(self):
    while max(self.pairs_points) < 12:
      print()
      print()
      self.deck = Deck()
      self.deck.shuffle_deck()
      self.deck.define_manilhas()
      self.play_round()
      for agent in self.agents:
        agent.mao = []
      print("Placar {}:{}".format(self.pairs_points[0], self.pairs_points[1]))
    
    if self.pairs_points[0] > self.pairs_points[1]:
      print("Dupla 1 ganhou o jogo!")
    else:
      print("Dupla 2 ganhou o jogo!")


  def play_round(self):
    while True:
      self.schedule = BaseScheduler(self)
      for agent in self.agents:
        self.schedule.add(agent)
      self.schedule.step()
      if not self.play:
        print('--------------------------')
        print('Vira: ', self.deck.get_vira())
        print('--------------------------')
        continue
      self.step_point()
      self.play = []
      print('--------------------------')
      if pair := self.has_partial_winner():
        self.partial_pair_points = [0,0]
        self.pairs_points[int(pair)] += 1
        break

  def step_point(self):
    best_play = self.get_winning_play(self.get_winning_play(self.play[0], self.play[2]), 
                                      self.get_winning_play(self.play[1], self.play[3]))
    self.partial_pair_points[best_play['pair']] += 1
    print("Ponto da dupla", best_play['pair'] + 1)

  def has_partial_winner(self):
    if self.partial_pair_points[0] == 2:
      print("Dupla 1 marcou 1 ponto!")
      return '0'
    if self.partial_pair_points[1] == 2:
      print("Dupla 2 marcou 1 ponto!")
      return '1'
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