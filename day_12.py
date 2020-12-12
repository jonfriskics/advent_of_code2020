import re
import os
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_12.txt', 'r')
directions = file.read().strip().split('\n')

compass = ["E","S","W","N"]
pos = (0,0)
facing = "E"

def manhatten_distance(x_start, y_start, x_end, y_end):
  return (abs(x_start - x_end) + abs(y_start - y_end))

for direction in directions:
  lookup = re.search('(\w)(\d+)', direction)
  action = lookup.groups()[0]
  units = int(lookup.groups()[1])
  if(action == "N"):
    pos = (pos[0], pos[1] + units)
  elif(action == "S"):
    pos = (pos[0], pos[1] - units)
  elif(action == "E"):
    pos = (pos[0] + units, pos[1])
  elif(action == "W"):
    pos = (pos[0] - units, pos[1])
  elif(action == "L"):
    idx = compass.index(facing)
    movement = 0
    if(units == 90):
      movement = 1
    elif(units == 180):
      movement = 2
    elif(units == 270):
      movement = 3
    direction_moved = idx - movement
    if(direction_moved == -1):
      idx = 3
    elif(direction_moved == -2):
      idx = 2
    elif(direction_moved == -3):
      idx = 1
    else:
      idx = direction_moved
    facing = compass[idx]
  elif(action == "R"):
    idx = compass.index(facing)
    movement = 0
    if(units == 90):
      movement = 1
    elif(units == 180):
      movement = 2
    elif(units == 270):
      movement = 3
    direction_moved = idx + movement
    if(direction_moved == 4):
      idx = 0
    elif(direction_moved == 5):
      idx = 1
    elif(direction_moved == 6):
      idx = 2
    else:
      idx = direction_moved
    facing = compass[idx]
  elif(action == "F"):
    if(facing == "E"):
      pos = (pos[0] + units, pos[1])
    elif(facing == "W"):
      pos = (pos[0] - units, pos[1])
    elif(facing == "N"): 
      pos = (pos[0], pos[1] + units)
    elif(facing == "S"):
      pos = (pos[0], pos[1] - units)

print(f'star1: {manhatten_distance(0,0,pos[0],pos[1])}')

waypoint = (10, 1)
ship = (0,0)
facing = "E"

for direction in directions:
  lookup = re.search('(\w)(\d+)', direction)
  action = lookup.groups()[0]
  units = int(lookup.groups()[1])
  if(action == "N"):
    waypoint = (waypoint[0], waypoint[1] + units)
  elif(action == "S"):
    waypoint = (waypoint[0], waypoint[1] - units)
  elif(action == "E"):
    waypoint = (waypoint[0] + units, waypoint[1])
  elif(action == "W"):
    waypoint = (waypoint[0] - units, waypoint[1])
  elif(action == "R"):
    if(units == 90):
      waypoint = (waypoint[1], -waypoint[0])
    elif(units == 180):
      waypoint = (-waypoint[0], -waypoint[1])
    elif(units == 270):
      waypoint = (-waypoint[1], waypoint[0])
  elif(action == "L"):
    if(units == 90):
      waypoint = (-waypoint[1], waypoint[0])
    elif(units == 180):
      waypoint = (-waypoint[0], -waypoint[1])
    elif(units == 270):
      waypoint = (waypoint[1], -waypoint[0])
  elif(action == "F"):
    if(facing == "E"):
      ship = (ship[0] + waypoint[0] * units, ship[1] + waypoint[1] * units)
    elif(facing == "W"):
      ship = (ship[0] - waypoint[0] * units, ship[1] - waypoint[1] * units)
    elif(facing == "N"):
      ship = (ship[0] + waypoint[0] * units, ship[1] + waypoint[1] * units)
    elif(facing == "S"):
      ship = (ship[0] - waypoint[0] * units, ship[1] - waypoint[1] * units)

print(f'star2: {manhatten_distance(0,0,ship[0],ship[1])}')