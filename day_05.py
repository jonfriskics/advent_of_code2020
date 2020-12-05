import math
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_05.txt', 'r')
seats = file.read().strip().split('\n')

star1 = 0
star2 = 0
ids = set()

for seat in seats:
  step1 = seat[0]
  step2 = seat[1]
  step3 = seat[2]
  step4 = seat[3]
  step5 = seat[4]
  step6 = seat[5]
  step7 = seat[6]
  col1 = seat[7]
  col2 = seat[8]
  col3 = seat[9]

  r = [i for i in range(128)]
  
  if(step1 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step1 == "B"):
    c = len(r)//2
    r = r[c:]
  
  if(step2 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step2 == "B"):
    c = len(r)//2
    r = r[c:]

  if(step3 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step3 == "B"):
    c = len(r)//2
    r = r[c:]

  if(step4 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step4 == "B"):
    c = len(r)//2
    r = r[c:]

  if(step5 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step5 == "B"):
    c = len(r)//2
    r = r[c:]

  if(step6 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step6 == "B"):
    c = len(r)//2
    r = r[c:]

  if(step7 == "F"):
    c = len(r)//2
    r = r[:c]
  elif(step7 == "B"):
    c = len(r)//2
    r = r[c:]

  cols = [i for i in range(8)]

  if(col1 == "L"):
    c = len(cols)//2
    cols = cols[:c]
  elif(col1 == "R"):
    c = len(cols)//2
    cols = cols[c:]

  if(col2 == "L"):
    c = len(cols)//2
    cols = cols[:c]
  elif(col2 == "R"):
    c = len(cols)//2
    rcols = cols[c:]

  if(col3 == "L"):
    c = len(cols)//2
    cols = cols[:c]
  elif(col3 == "R"):
    c = len(cols)//2
    cols = cols[c:]
  
  row = int(r[0])
  col = int(cols[0])
  ids.add(row * 8 + col)

print(f'star1: {max(ids)}')
