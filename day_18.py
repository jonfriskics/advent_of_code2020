import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_18.txt', 'r')
lines = file.read().strip().split('\n')

def solve_for_vals(l):
  vals_left = True
  while(vals_left):
    vals_lookup = re.search('(\d+)\s*([\*\+])\s*(\d+)', l)
    after_vals = l[vals_lookup.end():]
    one = vals_lookup.groups()[0]
    operator = vals_lookup.groups()[1]
    two = vals_lookup.groups()[2]
    if(operator == '+'):
      solve = int(one) + int(two)
    elif(operator == '*'):
      solve = int(one) * int(two)
    else:
      print("something wrong with operator")
    print(f'solved {solve}')
    l = (f'{solve} {after_vals}')
    vals_left = re.search('(\d+)\s*([\*\+])\s*(\d+)', l)
  return l

star1 = 0
for line in lines:
  parens_found = re.search('\)',line)
  if(parens_found):
    p_found = True
    while(p_found):
      inner_parens_lookup = re.search('\([\d\s\*\+]+\)', line)
      print(f'line {line}')
      if(inner_parens_lookup):        
        before_parens = line[0:inner_parens_lookup.start()]
        print(inner_parens_lookup)
        after_parens = line[inner_parens_lookup.end():]
        print(f'before_parens {before_parens}, after_parens {after_parens}')
        solve = solve_for_vals(line[inner_parens_lookup.start():inner_parens_lookup.end()-1])
        line = (f'{before_parens} {solve} {after_parens}')
        print(line)
        p_found = re.search('\)', line)
      else:
        p_found = None 
        line = line[0:len(line)-2]     
  
  star1 += int(solve_for_vals(line))
  
print(f'star1: {star1}')
