from deck import Deck
from player import Player

class Round(object):
  def __init__(self, players):
    self.players = players
    self.players_in = players
    self.deck = Deck()
    # self.
    self.pot = 0

  # def 

def main():
  player_one = Player('David')
  player_two = Player('Patrick')
  players = [player_one, player_two]
  

if __name__ == '__main__':
  main()
