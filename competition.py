import numpy as np
import week
import pdb
from operator import attrgetter

class Competition: 
  def __init__(self, sched, teams):
    weeks = []
    for i in range(sched.nweeks):
      games = []
      for j in range(sched.nteams//2):
        games.append(sched.get_game(i, j))
      weeks.append(week.Week(games))
    self.weeks = weeks
    # self.teams = [teams[sched.team_order[i]] for i in range(sched.nteams)]
    self.teams = teams
    self.set_scores()
    self.compute()

  def set_scores(self):
    for team in self.teams:
      for iweek, val in team.scores.items():
        week = self.weeks[iweek-1]
        week.set_score(team.idx, val)

  def compute(self):
    for i, week in enumerate(self.weeks):
      for game in week.games:
        winner = game.get_winner_id()
        loser = game.get_loser_id()
        self.teams[winner].add_win(i)
        self.teams[loser].add_loss(i)

    self.teams = sorted(self.teams, key=attrgetter('wins', 'points_for'), reverse=True)


  def __str__(self):
    str = ""
    # for i, week in enumerate(self.weeks):
    #     str += "week {}\n".format(i+1)
    #     str += week.__str__()
    #     str += "\n"
    for team in self.teams:
      str += team.__str__()
      str += "\n"
    return str
