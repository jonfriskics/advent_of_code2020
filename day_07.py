import re
import os
from collections import ChainMap

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_07.txt', 'r')
lines = file.read().strip().split('\n')

bags = {}

for line in lines:
  split_line = line.split(' contain ')
  bag_color = split_line[0]
  bags[bag_color] = {}
  if(split_line[1].find('no other bags') == -1):
    cb = list()
    for contained_bags in split_line[1].split(', '):
      lookup = re.search('(\d+)\s(.+)', contained_bags)
      qty = lookup.group(1).strip()
      bag = lookup.group(2).strip('.')
      if(bag[-1] != 's'):
        bag = bag + 's'
      c = str(bag_color)
      cb.append({bag: qty})
    bags[c] = dict(ChainMap(*cb))

#print(bags)

def check_for_gold(bag):
  #print(f'---- {bag} | {bags[bag]} ----')
  if(len(bags[bag].keys()) == 0):
    #print(f'{bag} is length zero for bag {bag}')
    return False
  if("shiny gold" in bag):
    return True
  else:
    found_shiny = False
    for k, v in bags[bag].items():
      #print(f'k: {k} v: {v}')
      if(check_for_gold(k)):
        found_shiny = True
    return found_shiny

star1 = 0

for bag in bags.keys():
  #print(f'bag in loop {bag}')
  found = check_for_gold(bag)
  if(found):
    star1 += 1

def number_of_bags(bag):
  sum = 0
  for k, v in bags[bag].items():
    sum += int(v) * (number_of_bags(k) + 1)
  return sum

star2 = number_of_bags("shiny gold bags")

print(f'star1: {star1 - 1}')
print(f"star2: {star2}")
