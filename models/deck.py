from models.card import Card
from models.rank import Rank
from models.suit import Suit
from random import shuffle

class Deck(object):
  def __init__(self):
    self.cards = []
    for rank in Rank:
      for suit in Suit:
        self.cards.append(Card(rank, suit))
    shuffle(self.cards)

  def deal_card(self):
    if self.is_empty():
      return None
    card = self.cards[0]
    del self.cards[0]
    return card

  def is_empty(self):
    return len(self.cards) == 0

  def size(self):
    return len(self.cards)
