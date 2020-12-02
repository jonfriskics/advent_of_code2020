import math
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_02.txt', 'r')
input = file.read().strip().split('\n')

star1_match_found = 0
star2_match_found = 0

for i in input:
  split = i.split(" ")
  range = split[0]
  char = split[1][0]
  password = split[2]
  
  min = range.split("-")[0]
  max = range.split("-")[1]
  
  matches = re.findall(char, password)
  if(int(min) <= len(matches) and len(matches) <= int(max)):
    star1_match_found += 1
    
  min_shifted = int(min)-1
  max_shifted = int(max)-1
  
  if((password[min_shifted] == char and password[max_shifted] != char) or (password[min_shifted] != char and password[max_shifted] == char)):
    if(password[min_shifted] == char and password[max_shifted] == char):
      continue
    else:
      star2_match_found += 1

print(f"star 1 matches found {star1_match_found}")
print(f"star 2 matches found {star2_match_found}")