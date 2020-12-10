import re
import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_10.txt', 'r')
joltages = [int(i) for i in file.read().strip().split('\n')]

jolts_adapter = max(joltages) + 3

joltages.sort()

charging_outlet_rating = 0

#print(joltages, jolts_adapter)

diffs_of_one = []
diffs_of_two = []
diffs_of_three = []

current_voltage = charging_outlet_rating
for i in joltages:
  #print(f'current_voltage {current_voltage} \t i {i}')
  if(current_voltage < i <= current_voltage + 3):
    if(i-current_voltage == 1):
      diffs_of_one.append(i)
    elif(i-current_voltage == 2):
      diffs_of_two.append(i)
    elif(i-current_voltage == 3):
      diffs_of_three.append(i)
  current_voltage = i

arrangements = defaultdict(int, {0:1})

joltages.insert(0, 0)
joltages.append(max(joltages) + charging_outlet_rating)

n = 0
for i in joltages:
  current_voltage = i
  for j in range(n-3,n):
    if(current_voltage - joltages[j] == 1):
      print(
          f'n {n} \t j {j} \t cv {current_voltage} \t j[j] {joltages[j]} \t diff {current_voltage - joltages[j]} \t arrlen {len(arrangements.values())} \t arr[j] {arrangements[j]} \t *******')
      arrangements[n] += arrangements[j]
    elif(current_voltage - joltages[j] == 2):
      print(
          f'n {n} \t j {j} \t cv {current_voltage} \t j[j] {joltages[j]} \t diff {current_voltage - joltages[j]} \t arrlen {len(arrangements.values())} \t arr[j] {arrangements[j]} \t *******')
      arrangements[n] += arrangements[j]
    elif(current_voltage - joltages[j] == 3):
      print(
          f'n {n} \t j {j} \t cv {current_voltage} \t j[j] {joltages[j]} \t diff {current_voltage - joltages[j]} \t arrlen {len(arrangements.values())} \t arr[j] {arrangements[j]} \t *******')
      arrangements[n] += arrangements[j]
    else:
      print(
          f'n {n} \t j {j} \t cv {current_voltage} \t j[j] {joltages[j]} \t diff {current_voltage - joltages[j]} \t arrlen {len(arrangements.values())} \t arr[j] {arrangements[j]}')

  n+= 1

print(f'star1: {len(diffs_of_one) * (len(diffs_of_three)+1)}')
print(f'star2: {max(arrangements.values())}')
