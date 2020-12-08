import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_08.txt', 'r')
instructions = file.read().strip().split('\n')

i = []
n = 0
for instruction in instructions:
  operation = instruction.split(' ')[0]
  argument = instruction.split(' ')[1]
  i.append({'id': n, 'op': operation, 'arg': argument})
  n += 1

def already_ran(inst, runs, accumulator):
  if(inst in runs):
    print(accumulator)
    exit()

def run_program(i):
  runs = []
  accumulator = 0
  x = 0
  while x < 10000:
    # print(i[x])
    if(x == len(i)):
      return accumulator
    if(i[x]['op'] == 'nop'):
      x += 1
    elif(i[x]['op'] == 'acc'):
      accumulator += int(i[x]['arg'])
      x += 1
    elif(i[x]['op'] == 'jmp'):
      direction = re.search('^(\-|\+)(\d+)', i[x]['arg'])
      if(direction.group(1) == '+'):
        x = x + int(direction.group(2))
      else:
        x = x - int(direction.group(2))
    if(already_ran(i[x]['id'], runs, accumulator)):
      return None
    else:
      runs.append(i[x]['id'])

run_program(i)