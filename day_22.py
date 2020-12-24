import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_22.txt', 'r')
players = file.read().strip().split('\n\n')

player1 = []
player2 = []

for i, player in enumerate(players):
  player_split = player.split('\n')
  for j, rows in enumerate(player_split):
    if j == 0:
      continue
    if i == 0:
      player1.append(int(rows))
    elif i == 1:
      player2.append(int(rows))

n = 0
while(len(player1) != 0 and len(player2) != 0):
  if(player1[0] > player2[0]):
    player1.append(player1[0])
    player1.append(player2[0])
    player1.pop(0)
    player2.pop(0)
  elif(player2[0] > player1[0]):
    player2.append(player2[0])
    player2.append(player1[0])
    player1.pop(0)
    player2.pop(0)
  n += 1
  print(n+1, player1, player2)

score = 0
if(len(player1) != 0):
  player1.reverse()
  for i, card in enumerate(player1):
    score += card * (i+1)
elif(len(player2) != 0):
  player2.reverse()
  for i, card in enumerate(player2):
    score += card * (i+1)

print(score)
