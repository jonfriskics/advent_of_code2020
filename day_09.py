import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_09.txt', 'r')
numbers = file.read().strip().split('\n')

star1 = 0
star2 = 0

preamble_length = 25

def check_sum(last_few, number_to_check):
  sums = []
  #print(last_few, number_to_check)
  for i in range(len(last_few)):
    for j in range(len(last_few)):
      sums.append(int(last_few[i]) + int(last_few[j]))
  #print(f'sums: {sums}')
  if(int(number_to_check) in sums):
    #print(f"found {number_to_check}")
    return True
  else:
    return False

idx = preamble_length

for i in range(preamble_length, len(numbers)):
  #print(i)
  if(check_sum(numbers[i-preamble_length:i], numbers[i]) == False):
    star1 = numbers[i]
  else:
    pass

print(f'star 1 {star1}')

number_ints = [int(n) for n in numbers]

for i in range(len(number_ints)-1):
  starting_number = number_ints[i]
  for j in range(i+1, len(number_ints)):
    #print(f'i {i} j {j} starting_number {starting_number}')
    if starting_number == int(star1):
      #print(f'i {i} j {j}')
      star2 = min(number_ints[i: j]) + max(number_ints[i: j])
      print(star2)
      break
    starting_number += number_ints[j]
