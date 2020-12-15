import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_14.txt', 'r')
lines = file.read().strip().split('\n')

mask = ''
n = 0
full_memory = {}
for line in lines:
  if(line[0:3] == 'mas'):
    mask = line[7:]
  elif(line[0:3] == 'mem'):
    lookup_register = re.search('\d+',line[0:])
    memory_register = lookup_register.group()
    lookup_value = re.search('\=\s(\d+)',line[0:])
    memory_value = lookup_value.groups()[0]
    binary_memory = "{0:b}".format(int(memory_value))
    str_binary_memory = str(binary_memory)

    l = []
    for x in range(0,36):
      l.append('0')
    for i, x in enumerate(str_binary_memory[::-1]):
      l[i] = x

    for i, m in enumerate(mask[::-1]):
      #print(i, m, l[i])
      if(m == "X"):
        l[i] = l[i]
      elif(m == "0"):
        l[i] = "0"
      elif(m == "1"):
        l[i] = "1"
    
    s = l[::-1]
    #print("".join(s))
    final_value = int("".join(s), 2)
    full_memory[memory_register] = final_value

star1 = 0

for k, v in full_memory.items():
  star1 += v

print(f'star1: {star1}')
