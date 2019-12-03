import numpy as np

class Game: 
  def __init__(self, id1, id2):
    self.teams = (id1, id2)
    self.winner = None
    self.score = [0, 0]

  def set_score_by_id(self, idx, score):
    if self.teams[0] == idx:
      self.score[0] = score
    elif self.teams[1] == idx:
      self.score[1] = score
    else:
      raise Exception("team id does not match")
    self.update_winner()

  def update_winner(self):
    self.winner = self.score[1] > self.score[0]

  def set_score(self, score1, score2):
    self.score = (score1, score2)
    self.update_winner()

  def set_winner(self, i):
    if i != 0 and i != 1:
      raise Exception("i should be 0 or 1")
    self.winner = i
    self.score = None

  def random_winner(self):
    n = 1
    p = 0.5
    self.winner = np.random.binomial(n,p)
    self.score = None

  def get_loser(self):
    return (self.winner + 1) % 2

  def get_winner_id(self):
    return self.teams[self.winner]

  def get_loser_id(self):
    return self.teams[self.get_loser()]

  def get_winner_score(self):
    return self.score[self.winner]

  def get_loser_score(self):
    return self.score[self.get_loser()]

  def __str__(self):
    if self.winner is None:
        str = "{} vs {}".format(self.teams[0], self.teams[1])
    else:
        str = "{} defeats {}".format(self.get_winner_id(), self.get_loser_id())
        if self.score is not None:
          str += " {} - {}".format(self.get_winner_score(), self.get_loser_score())

    return str


if __name__== "__main__":
  g = Game(0, 1)
  print(g)
  g.set_score(110, 95)
  print(g)
  g.set_score(87, 132)
  print(g)
  g.set_winner(0)
  print(g)
  g.set_winner(1)
  print(g)
  g.random_winner()
  print(g)
  g.random_winner()
  print(g)
  g.random_winner()
  print(g)