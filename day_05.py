import math
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_05.txt', 'r')
seats = file.read().strip().split('\n')

star1 = 0
star2 = 0
ids = set()

for seat in seats:
  rows_range = [0, 127]
  for letter in seat[0:7]:
    if letter == "F":
      rows_range[1] = rows_range[1] - (rows_range[1] + 1 - rows_range[0])/2
    elif letter == "B":
      rows_range[0] = rows_range[0] + (rows_range[1] + 1 - rows_range[0])/2

  cols_range = [0, 7]
  for letter in seat[7:10]:
    if letter == "L":
      cols_range[1] = cols_range[1] - (cols_range[1] + 1 - cols_range[0])/2
    elif letter == "R":
      cols_range[0] = cols_range[0] + (cols_range[1] + 1 - cols_range[0])/2

  row = int(rows_range[1])
  column = int(cols_range[1])
  ids.add(row * 8 + column)

print(f'star1: {max(ids)}')

for missing_seat in range(128*8):
  if (missing_seat not in ids
      and missing_seat - 1 in ids
      and missing_seat + 1 in ids
    ):
    print(f'star2: {missing_seat}')
