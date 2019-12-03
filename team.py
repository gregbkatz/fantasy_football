import numpy as np

class Team: 
  def __init__(self, idx, name):
    self.name = name
    self.idx = idx
    self.scores = {}
    self.record = {}
    self.wins = None
    self.losses = None
    self.points_for = None

  def set_scores(self, scores):
    self.scores = scores
    self.points_for = sum(self.scores.values())

  def add_win(self, week):
    self.add_result(week, 1)

  def add_loss(self, week):
    self.add_result(week, 0)

  def add_result(self, week, result):
    self.record[week] = result
    self.compute()

  def compute(self):
    self.wins = sum(self.record.values())
    self.losses = len(self.record) - self.wins

  def __str__(self):
    str = ""
    str += "{} {}: {}-{} {}".format(
      self.idx, 
      self.name, 
      self.wins, 
      self.losses, 
      self.points_for
      )
    # str += self.scores.__str__()
    return str


if __name__== "__main__":
  t = Team(0, "Greg")