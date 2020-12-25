import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_25.txt', 'r')
rows = file.read().strip().split('\n')

card_key = "5764801"
door_key = "17807724"

for i, row in enumerate(rows):
  if(i == 0):
    card_key = row
  elif(i == 1):
    door_key = row

print(card_key, door_key)

subject_number = 7
card_loop_size = 1
door_loop_size = 1
card_val = 1
door_val = 1

for i in range(0,20000000):
  card_val = card_val * subject_number
  card_val = card_val % 20201227
  #print(card_val)
  if(int(card_val) == int(door_key)):
    card_loop_size = i
    break

print(f'card_loop_size {card_loop_size+1}')

for i in range(0,20000000):
  door_val = door_val * subject_number
  door_val = door_val % 20201227
  if(int(door_val) == int(card_key)):
    door_loop_size = i
    break

print(f'door_loop_size {door_loop_size+1}')

door_subj_number = door_key
new_val = 1

for i in range(0,int(door_loop_size)+1):
  new_val = new_val * int(door_subj_number)
  new_val = int(new_val) % 20201227

print(new_val)
