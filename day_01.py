import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_01.txt', 'r')
input = file.read().split('\n')
# input = file.read().strip()

sum_star01 = 0
sum_star02 = 0
