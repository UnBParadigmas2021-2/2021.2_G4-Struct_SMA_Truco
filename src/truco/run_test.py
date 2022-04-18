from random import shuffle
# from Game import Game
from Deck import Deck 
from PlayerModel import PlayerModel


if __name__ == '__main__':
  # qtde_players = int(input("Digite a quantidade de jogadores: "))
  # game = Game(qtde_players)

  deck = Deck()
  deck.shuffle_deck()
  # print(deck.cards[0].weight)
  deck.define_vira(deck)
  manilha = deck.define_manilha()
  # print("manilha: " + str(manilha))
  deck.define_manilhas(manilha)

  # print(deck.manilhas)
  # print("1 " + str(deck.manilhas[0].weight))
  # print("2 " + str(deck.manilhas[1].weight))
  # print("3 " + str(deck.manilhas[2].weight))
  # print("4 " + str(deck.manilhas[3].weight))

  # for i in range(game.qtde_players):
  #   nome = int(input("Digite o nome jo jogador: "+ str(i)))
  #   jogador[i] = game.criar_player(nome)

  player = PlayerModel(4, deck)
  player.step()
