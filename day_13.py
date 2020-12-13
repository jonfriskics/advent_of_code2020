from functools import reduce
import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_13.txt', 'r')
bus_routes = file.read().strip().split('\n')

earliest_timestamp = bus_routes[0]

active_ids = []
for id in bus_routes[1].split(','):
  lookup = re.search('\d+', id)
  if(lookup != None):
    active_ids.append(lookup.group().strip())

routes = {}
for id in active_ids:
  for x in range(0,1000000):
    if (x * int(id)) > int(earliest_timestamp):
      routes[id] = x *int(id)
      break

sorted_routes = sorted(routes.items(), key=lambda x: x[1])
print(f'star1: {int(sorted_routes[0][0]) * (int(sorted_routes[0][1]) - int(earliest_timestamp))}')

# implementation copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
  sum = 0
  prod = reduce(lambda a, b: a*b, n)
  for n_i, a_i in zip(n, a):
    p = prod // n_i
    sum += a_i * mul_inv(p, n_i) * p
  return sum % prod


def mul_inv(a, b):
  b0 = b
  x0, x1 = 0, 1
  if b == 1:
    return 1
  while a > 1:
    q = a // b
    a, b = b, a % b
    x0, x1 = x1 - q * x0, x0
  if x1 < 0:
    x1 += b0
  return x1

a = []
b = []
for i, timestamp in enumerate(active_ids):
  if(timestamp):
    timestamp = int(timestamp)
  a.append(timestamp)
  b.append(timestamp-i)

print(f'star2: {chinese_remainder(a,b)}')
