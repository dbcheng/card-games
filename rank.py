from enum import Enum

class Rank(Enum):
  """docstring for Rank"""
  two = 2
  three = 3
  four = 4
  five = 5
  six = 6
  seven = 7
  eight = 8
  nine = 9
  ten = 10
  jack = 11
  queen = 12
  king = 13
  ace = 14

  def __eq__(self, other):
    return self.value == other.value

  def __gt__(self, other):
    return self.value > other.value

  def __ge__(self, other):
    return self.value >= other.value

  def __lt__(self, other):
    return self.value < other.value

  def __le__(self, other):
    return self.value <= other.value

  def __str__(self):
    return self.name.upper()
