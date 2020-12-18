import re
import os
import copy
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_17.txt', 'r')
lines = file.read().strip().split('\n')

# nope