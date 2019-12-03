import schedules
import team
import competition
import pdb
import numpy as np
import operator

np.set_printoptions(precision=2, suppress=True)


if __name__== "__main__":

  raw_teams = {}
  with open("blue_dot_scores.csv") as f:
    for line in f:
      words = line.split(",")
      week = int(words[0])
      name = words[1]
      score = float(words[2])
      if name not in raw_teams:
        raw_teams[name] = {}
      raw_teams[name][week] = score

  nschedules = 10000

  teams = []
  team_stats = {}
  for i,name in enumerate(raw_teams.keys()):
    teams.append(team.Team(i, name))
    teams[i].set_scores(raw_teams[name])
    if name not in team_stats:
      team_stats[name] = {}
    team_stats[name]["wins"] = np.zeros((nschedules), dtype=np.int32)
    team_stats[name]["ranks"] = np.zeros((nschedules), dtype=np.int32)


  nteams = len(teams)
  nweeks = 12
  scheds = schedules.Schedules(nteams, nweeks, nschedules)
  for j, sched in enumerate(scheds.schedules):
    comp = competition.Competition(sched, teams)
    for i, team in enumerate(comp.teams):
      team_stats[team.name]["wins"][j] = team.wins
      team_stats[team.name]["ranks"][j] = i
    # print(comp)

  for team, stats in team_stats.items():
    team_stats[team]["pdf"] = np.bincount(stats['ranks'], minlength=nteams)/nschedules
    team_stats[team]["cdf"] = np.cumsum(team_stats[team]["pdf"])
    # print("{:20}".format(team), team_stats[team]["pdf"] )



  # team_stats = sorted(team_stats.items(), key = lambda kv: kv[1]["wins"].mean(), reverse=True)
  team_stats = sorted(team_stats.items(), key = lambda kv: kv[1]["cdf"][3], reverse=True)
  for team, stats in team_stats:
    print("{:10}{:8.2f}{:8.2f}   ".format(
      team, stats["wins"].mean(), stats["ranks"].mean()+1), 
    stats["cdf"], stats["pdf"] )



