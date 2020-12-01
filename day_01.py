import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_01.txt', 'r')
input = file.read().strip().split('\n')

star1_input = [int(i) for i in input]
star1_input.sort()

for i in range(len(star1_input)):
  for j in range(len(star1_input)-i):
    if(star1_input[i] + star1_input[j] == 2020):
      print("star 1 ", star1_input[i] * star1_input[j])
    for z in range(len(star1_input)-j):
      if(star1_input[i] + star1_input[j] + star1_input[z] == 2020):
        print("star 2 ", star1_input[i] * star1_input[j] * star1_input[z])
