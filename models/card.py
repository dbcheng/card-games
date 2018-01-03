class Card(object):
  """docstring for Card"""
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def is_same_suit(self, card):
    return self.suit == card.suit

  def is_same_rank(self, card):
    return self.rank == card.rank

  def __str__(self):
    return str(self.rank) + " of " + str(self.suit)

  def __repr__(self):
    return str(self.rank) + " of " + str(self.suit)

  def __eq__(self, card):
    return self.suit == card.suit and self.rank == card.rank

  def __gt__(self, card):
    return self.rank > card.rank

  def __ge__(self, card):
    return self.rank >= card.rank

  def __lt__(self, card):
    return self.rank < card.rank

  def __lt__(self, card):
    return self.rank <= card.rank
