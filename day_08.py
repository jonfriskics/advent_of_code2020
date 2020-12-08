import re
import os
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_08.txt', 'r')
instructions = file.read().strip().split('\n')

star1 = 0

i = []
n = 0
for instruction in instructions:
  operation = instruction.split(' ')[0]
  argument = instruction.split(' ')[1]
  i.append({'id': n, 'op': operation, 'arg': argument})
  n += 1

def already_ran(id, runs, accumulator):
  #print(f'already_ran id {id} runs {runs} accumulator {accumulator}')
  if(id in runs):
    return True
  else:
    return False

def run_program(a):
  runs = []
  accumulator = 0
  x = 0
  while True:
    if(x >= len(a)):
      return accumulator

    if(already_ran(a[x]['id'], runs, accumulator)):
      return None 
    else:
      runs.append(a[x]['id'])

    if(a[x]['op'] == 'nop'):
      x += 1
    elif(a[x]['op'] == 'acc'):
      accumulator += int(a[x]['arg'])
      x += 1
    elif(a[x]['op'] == 'jmp'):
      direction = re.search('^(\-|\+)(\d+)', a[x]['arg'])
      if(direction.group(1) == '+'):
        x = x + int(direction.group(2))
      else:
        x = x - int(direction.group(2))

count = 0
for x in range(len(i)):
  i_copy = copy.deepcopy(i)
  #print(f'x {x} i {i} icopy {i_copy}')
  if(i_copy[x]['op'] == 'jmp'):
    i_copy[x]['op'] = 'nop'
  elif(i_copy[x]['op'] == 'nop'):
    i_copy[x]['op'] = 'jmp'
  #print(i, i_copy)
  run = run_program(i_copy)
  if(run != None):
    print(run)
  count += 1
