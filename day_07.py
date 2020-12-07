import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_07.txt', 'r')
lines = file.read().strip().split('\n')

bags = {}

for line in lines:
  split_line = line.split(' contain ')
  bag_color = split_line[0]
  bags[bag_color] = list()
  if(split_line[1].find('no other bags') == -1):
    for contained_bags in split_line[1].split(', '):
      lookup = re.search('(\d+)\s(.+)', contained_bags)
      qty = lookup.group(1).strip()
      bag = lookup.group(2).strip('.')
      if(bag[-1] != 's'):
        bag = bag + 's'
      bags[bag_color].append(bag)

# print(bags)

def check_for_gold(bag):
  # print(bag)
  # print(bag, bags[bag])
  if(len(bags[bag]) == 0):
    return False
  if("shiny gold bags" in bags[bag]):
    return True
  for contained_bag in bags[bag]:
    if(check_for_gold(contained_bag)):
      return True

star1 = 0

for bag in bags:
  # print(bag)
  found = check_for_gold(bag)
  if(found):
    star1 += 1

print(star1)
