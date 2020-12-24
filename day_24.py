import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_24.txt', 'r')
rows = file.read().strip().split('\n')

def Remove(tuples):
  tuples = [t for t in tuples if t]
  return tuples

reference_x = 0
reference_y = 0

tiles = []
flipped_tiles = {}

for row in rows:
  matches = re.findall('(nw)|(ne)|(e)|(se)|(sw)|(w)', row)
  cleaned_matches = []
  for match in matches:
    cleaned_matches.append(Remove(match)[0])
  #print(cleaned_matches)
  reference_x = 0
  reference_y = 0

  for match in cleaned_matches:
    if match == 'w':
      reference_x -= 2
    elif match == 'e':
      reference_x += 2
    elif match == 'nw':
      reference_x -= 1
      reference_y += 1
    elif match == 'ne':
      reference_x += 1
      reference_y += 1
    elif match == 'se':
      reference_x += 1
      reference_y -= 1
    elif match == 'sw':
      reference_x -= 1
      reference_y -= 1
  
  loc = hash(f'{reference_x} {reference_y}')
  #print(reference_x, reference_y, loc)

  if(loc in flipped_tiles.keys()):
    if(flipped_tiles[loc] == True):
      flipped_tiles[loc] = False
    else:
      flipped_tiles[loc] = True
  else:
    flipped_tiles[loc] = True

print(len([truth for truth in flipped_tiles.values() if(truth == True)]))
