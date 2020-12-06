import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_06.txt', 'r')
questions = file.read().strip().split('\n\n')

questions_answered_yes = 0
all_answered_yes = 0

for question in questions:
  s = set()
  person = question.split("\n")
  for l in person:
    for x in l:
      s.add(x)
  questions_answered_yes += len(s)

alphabet = set()
for letter in range(97, 123):
  alphabet.add(chr(letter))

for question in questions:
  person = question.split("\n")
  for a in alphabet:
    matches = []
    for answers in person:
      if(a in answers):
        matches.append(True)
      else:
        matches.append(False)
    if(all(matches)):
      all_answered_yes += 1

print(f'star1: {questions_answered_yes}')
print(f'star2: {all_answered_yes}')