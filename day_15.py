import re
import os
import copy
from collections import defaultdict
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_15.txt', 'r')
lines = file.read().strip().split('\n')

input = [16,1,0,18,12,14,19]

keys = range(0, 30000000)
spoken = {key: None for key in keys}
#print(spoken)
spoken[0] = 16
spoken[1] = 1
spoken[2] = 0
spoken[3] = 18
spoken[4] = 12
spoken[5] = 14
spoken[6] = 19

for k,v in spoken.items():
  if(k < 7):
    continue
  #print(f'k {k} last spoken pos: {spoken[k-1]} counter {Counter(spoken.values())[spoken[k-1]]} count {Counter(spoken.values())[spoken[k-1]]} vals {spoken.values()}')
  if(Counter(spoken.values())[spoken[k-1]] < 2):
    spoken[k] = 0
  else:
    last_seen = False
    looking_for = spoken[k-1]
    starting = 2
    #print(f'k: {k} looking_for: {looking_for}')
    while last_seen == False:
      #print(f'----- lsp {k-1} starting {starting} ||| {spoken[k - starting]}')
      if(spoken[k - starting] == looking_for):
        #print(f'lsp {k-1} starting {starting}')
        last_seen = True
        spoken[k] = starting - 1
      else:
        starting += 1

print(spoken[29999999])
