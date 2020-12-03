import math
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_03.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0
star2 = 0

new_map = []

x = 0
y = 0

row_length = len(input[0])

# right 3, down 1
for row in range(len(input)):
  x = x + 3
  if(x >= row_length):
    x = x % row_length
  y = y + 1
  if(y >= len(input)):
    break
  if(input[y][x] == "#"):
    star1 += 1

trees_slope_1 = 0
trees_slope_2 = 0
trees_slope_3 = 0
trees_slope_4 = 0
trees_slope_5 = 0

x = 0
y = 0

# right 1, down 1
for row in range(len(input)):
  x = x + 1
  if(x >= row_length):
    x = x % row_length
  y = y + 1
  if(y >= len(input)):
    break
  if(input[y][x] == "#"):
    trees_slope_1 += 1

x = 0
y = 0

# right 3, down 1
for row in range(len(input)):
  x = x + 3
  if(x >= row_length):
    x = x % row_length
  y = y + 1
  if(y >= len(input)):
    break
  if(input[y][x] == "#"):
    trees_slope_2 += 1

x = 0
y = 0

# right 5, down 1
for row in range(len(input)):
  x = x + 5
  if(x >= row_length):
    x = x % row_length
  y = y + 1
  if(y >= len(input)):
    break
  if(input[y][x] == "#"):
    trees_slope_3 += 1

x = 0
y = 0

# right 7, down 1
for row in range(len(input)):
  x = x + 7
  if(x >= row_length):
    x = x % row_length
  y = y + 1
  if(y >= len(input)):
    break
  if(input[y][x] == "#"):
    trees_slope_4 += 1

x = 0
y = 0

# right 1, down 2
for row in range(len(input)):
  x = x + 1
  if(x >= row_length):
    x = x % row_length
  y = y + 2
  if(y >= len(input)):
    break
  if(input[y][x] == "#"):
    trees_slope_5 += 1

star2 = trees_slope_1 * trees_slope_2 * trees_slope_3 * trees_slope_4 * trees_slope_5
print(f"star 1 matches found {star1}")
print(f"star 2 matches found {star2}")
