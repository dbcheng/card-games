class Player(object):
  """docstring for Player"""
  def __init__(self, name, money):
    self.name = name
    self.money = money

  def __init__(self, name):
    self.name = name
    # Default is $500
    self.money = 500

  def lose_money(self, amt):
    self.money -= amt

  def gain_money(self, amt):
    self.money += amt
