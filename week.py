import numpy as np

class Week: 
  def __init__(self, games):
    self.games = games

  def find_by_id(self, team_id):
    for i, game in enumerate(self.games):
      if team_id in game.teams:
        return i
    raise Exception("id not found in week")

  def set_score(self, team_id, score):
    game_id = self.find_by_id(team_id)
    self.games[game_id].set_score_by_id(team_id, score)

  def __str__(self):
    str = ""
    for game in self.games:
        str += game.__str__()
        str += "\n"
    return str
