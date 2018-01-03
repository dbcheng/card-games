from enum import Enum

class Suit(Enum):
  """docstring for Rank"""
  clubs = 1
  diamonds = 2
  hearts = 3
  spades = 4

  def __eq__(self, other):
    return self.value == other.value

  def __str__(self):
    return self.name.upper()
