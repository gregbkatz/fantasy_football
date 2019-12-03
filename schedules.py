import numpy as np
import game
import pdb

def make_table(nteams):
  table = np.zeros((nteams-1, nteams), dtype=np.int32)
  for i in range(nteams-1):
    for j in range(nteams):
      if j == 0:
        col = 0
      else:
        col = (j + i - 1) % (nteams - 1) + 1
      table[i, col] = j
  return table

class Schedule:
  def __init__(self, nteams, nweeks, table=None):
    if nteams % 2 != 0:
      raise Exception("Must be even number of teams")
    self.nteams = nteams
    self.nweeks = nweeks
    if table is None:
      table = make_table(nteams)
    self.table = table
    if table.shape != (nteams-1, nteams):
      raise Exception("table size does not match nteams")
    self.random_schedule()

  def random_schedule(self):
    self.team_order = np.random.permutation(self.nteams).astype(np.int32)
    week_order = np.random.permutation(self.nteams - 1)
    reps, remainder = divmod(self.nweeks, (self.nteams - 1))
    week_order = np.concatenate((np.tile(week_order, reps), week_order[:remainder]))
    self.schedule = self.table[week_order, :]

  def get_game(self, week, i):
    team1 = self.schedule[week, i]
    team2 = self.schedule[week, i + self.nteams//2]
    return game.Game(self.team_order[team1], self.team_order[team2])

  def __str__(self):
    str = ""
    str += "nteams:{}".format(self.nteams)
    str += "\nnweeks:{}".format(self.nweeks)
    str += "\nschedule:"
    str += self.schedule.__str__()
    str += "\n"
    str += "\nteam_order:"
    str += self.team_order.__str__()
    return str

class Schedules: 
  def __init__(self, nteams, nweeks, nschedules):
    self.nteams = nteams
    self.nweeks = nweeks
    self.nschedules = nschedules
    self.table = make_table(nteams)
    self.schedules = [Schedule(nteams, nweeks, self.table) for i in range(nschedules)]

  def __str__(self):
    str = ""
    str += "nteams:{}".format(self.nteams)
    str += "\nnweeks:{}".format(self.nweeks)
    str += "\nnschedules:{}".format(self.nschedules)
    return str

if __name__== "__main__":
  nteams = 10
  nweeks = 12
  nschedules = 5
  s = Schedules(nteams, nweeks, nschedules)
  print(s)

