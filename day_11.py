import re
import os
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_11.txt', 'r')
raw_rows = file.read().strip().split('\n')

#print(rows)

star1 = 0
star2 = 0

row_length = len(raw_rows[0])

rows_as_numbers = [[None for i in range(
    len(raw_rows))] for j in range(row_length)]

for i in range(len(raw_rows)):
  for j in range(len(raw_rows[i])):
    if(raw_rows[i][j] == '.'):
      rows_as_numbers[i][j] = 0
    elif(raw_rows[i][j] == 'L'):
      rows_as_numbers[i][j] = 1
    elif(raw_rows[i][j] == '#'):
      rows_as_numbers[i][j] = 2

raw_rows = rows_as_numbers[:]

number_of_empty_adjacent = []
number_of_occupied_adjacent = []

def check_top_left_diagonal(rows, i, j):
  if(rows[i-1][j-1] == '1' or rows[i-1][j-1] == '0'):
    number_of_empty_adjacent.append(rows[i-1][j-1])
  else:
    number_of_occupied_adjacent.append(rows[i-1][j-1])


def check_top(rows,i,j):
  if(rows[i-1][j] == 1 or rows[i-1][j] == 0):
    number_of_empty_adjacent.append(rows[i-1][j])
  else:
    number_of_occupied_adjacent.append(rows[i-1][j])

def check_top_right_diagonal(rows, i, j):
  if(rows[i-1][j+1] == 1 or rows[i-1][j+1] == 0):
    number_of_empty_adjacent.append(rows[i-1][j+1])
  else:
    number_of_occupied_adjacent.append(rows[i-1][j+1])

def check_left(rows, i, j):
  if(i == 9 and j == 9):
    print("here")
    print(f'i {i} j {j} rowsij {rows[i][j]} rowsij-1 {rows[i][j-1]}')
  if(rows[i][j-1] == 1 or rows[i][j-1] == 0):
    number_of_empty_adjacent.append(rows[i][j-1])
  else:
    number_of_occupied_adjacent.append(rows[i][j-1])

def check_right(rows, i, j):
  if(rows[i][j+1] == 1 or rows[i][j+1] == 0):
    number_of_empty_adjacent.append(rows[i][j+1])
  else:
    number_of_occupied_adjacent.append(rows[i][j+1])

def check_bottom_left_diagonal(rows, i, j):
  if(rows[i+1][j-1] == 1 or rows[i+1][j-1] == 0):
    number_of_empty_adjacent.append(rows[i+1][j-1])
  else:
    number_of_occupied_adjacent.append(rows[i+1][j-1])

def check_bottom(rows, i, j):
  if(rows[i+1][j] == 1 or rows[i+1][j] == 0):
    number_of_empty_adjacent.append(rows[i+1][j])
  else:
    number_of_occupied_adjacent.append(rows[i+1][j])

def check_bottom_right_diagonal(rows, i, j):
  if(rows[i+1][j+1] == 1 or rows[i+1][j+1] == 0):
    number_of_empty_adjacent.append(rows[i+1][j+1])
  else:
    number_of_occupied_adjacent.append(rows[i+1][j+1])

copyable_rows = copy.deepcopy(raw_rows)
new_rows = copy.deepcopy(raw_rows)

for i in range(len(copyable_rows)):
  print("")
  for j in range(len(copyable_rows[i])):
    print(copyable_rows[i][j], end="")
print()

number_of_changed_rows = 0
keep_going = True

while keep_going == True:
  for i in range(0, len(copyable_rows)):
    for j in range(0, len(copyable_rows[i])):
      rows = copy.deepcopy(copyable_rows)
      number_of_empty_adjacent = []
      number_of_occupied_adjacent = []
      if(rows[i][j] == 1):
        if(i > 0 and j > 0 and i < len(rows)-1 and j < len(rows[i])-1):
          check_top_left_diagonal(rows, i, j)
          check_top(rows, i, j)
          check_top_right_diagonal(rows, i, j)
          check_left(rows, i, j)
          check_right(rows, i, j)
          check_bottom_left_diagonal(rows, i, j)
          check_bottom(rows, i, j)
          check_bottom_right_diagonal(rows, i, j)
        elif(i == len(rows)-1 and j == len(rows[i])-1):
          #for x in range(len(rows)):
          #  print("")
          #  for y in range(len(rows[i])):
          #    print(rows[x][y], end="")
          #print()
          #print(f'i {i} j {j} rowsij {rows[i][j]}')
          check_left(rows, i, j)
          check_top_left_diagonal(rows, i, j)
          check_top(rows, i, j)
        elif(i == 0 and j == 0):
          check_right(rows, i, j)
          check_bottom_right_diagonal(rows, i, j)
          check_bottom(rows, i, j)
        elif(i == 0 and j > 0 and j < len(rows[i])-1):
          check_left(rows, i, j)
          check_bottom_left_diagonal(rows, i, j)
          check_bottom(rows, i, j)
          check_bottom_right_diagonal(rows, i, j)
          check_right(rows, i, j)
        elif(i == 0 and j == len(rows[i])-1):
          check_left(rows, i, j)
          check_bottom_left_diagonal(rows, i, j)
          check_bottom(rows, i, j)
        elif(i == len(rows)-1 and j == 0):
          check_top(rows, i, j)
          check_top_right_diagonal(rows, i, j)
          check_right(rows, i, j)
        elif(i == len(rows)-1 and j > 0 and j < len(rows[i])-1):
          check_left(rows, i, j)
          check_top_left_diagonal(rows, i, j)
          check_top(rows, i, j)
          check_top_right_diagonal(rows, i, j)
          check_right(rows, i, j)
        elif(i > 0 and i < len(rows)-1 and j == 0):
          check_top(rows, i, j)
          check_top_right_diagonal(rows, i, j)
          check_right(rows, i, j)
          check_bottom_right_diagonal(rows, i, j)
          check_bottom(rows, i, j)
        elif(i > 0 and i < len(rows)-1 and j > 0 and j == len(rows[i])-1):
          check_top(rows, i, j)
          check_top_left_diagonal(rows, i, j)
          check_left(rows, i, j)
          check_bottom_left_diagonal(rows, i, j)
          check_bottom(rows, i, j)
      if(len(number_of_empty_adjacent) > 0):
        new_rows[i][j] = 2
        number_of_changed_rows += 1
  if(number_of_changed_rows == 0):
    keep_going = False
  else:
    keep_going = True
    print(number_of_changed_rows)
  copyable_rows = copy.deepcopy(new_rows)

print(number_of_changed_rows)
