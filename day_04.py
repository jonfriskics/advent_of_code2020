import math
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/inputs/day_04.txt', 'r')
passports = file.read().strip().split('\n\n')

star1 = 0
star2 = 0

#passports = 
for passport in passports:
  if(passport.find("byr") != -1 and passport.find("iyr") != -1 and passport.find("eyr") != -1 and passport.find("hgt") != -1 and passport.find("hcl") != -1 and passport.find("ecl") != -1 and passport.find("pid") != -1):
    star1 += 1
    
    passport = passport.split("\n")
    passport = " ".join(passport)
    
    byr_loc = passport.find("byr:")
    byr_val = re.search("(\d+)", passport[byr_loc:])
  
    iyr_loc = passport.find("iyr:")
    iyr_val = re.search("(\d+)", passport[iyr_loc:])

    eyr_loc = passport.find("eyr:")
    eyr_val = re.search("(\d+)", passport[eyr_loc:])

    hgt_loc = passport.find("hgt:")
    hgt_val = re.search("(\d+)(cm|in)", passport[hgt_loc:])

    hcl_loc = passport.find("hcl:")
    hcl_val = re.search("(\#[0-9a-f]{6})", passport[hcl_loc:])
    
    ecl_loc = passport.find("ecl:")
    ecl_val = re.search("(amb|blu|brn|gry|grn|hzl|oth)", passport[ecl_loc:])
    
    pid_loc = passport.find("pid:")
    pid_val = re.search("([0-9]{9})", passport[pid_loc:])
    
    if(
      byr_val is not None and
      iyr_val is not None and
      eyr_val is not None and
      hgt_val is not None and
      hcl_val is not None and
      ecl_val is not None and
      pid_val is not None and
      hgt_val.groups() is not None
    ):
      print('----------------------------')
      print(f'passport {passport}')
      print(f'byr_val {byr_val}')
      print(f'iyr_val {iyr_val}')
      print(f'eyr_val {eyr_val}')
      print(f'hgt_val {hgt_val}')
      print(f'hcl_val {hcl_val}')
      print(f'ecl_val {ecl_val}')
      print(f'pid_val {pid_val}')
      if(
        int(byr_val.group().strip()) >= 1920 and 
        int(byr_val.group().strip()) <= 2002 and
        int(iyr_val.group().strip()) >= 2010 and
        int(iyr_val.group().strip()) <= 2020 and
        int(eyr_val.group().strip()) >= 2020 and
        int(eyr_val.group().strip()) <= 2030
      ):
        if(hgt_val.groups()[1] == 'cm'):
          if(int(hgt_val.groups()[0]) >= 150 and int(hgt_val.groups()[0]) <= 193):
            star2 += 1
        elif(hgt_val.groups()[1] == 'in'):
          if(int(hgt_val.groups()[0]) >= 59 and int(hgt_val.groups()[0]) <= 76):
            star2 += 1

print(f"star 1 matches found {star1}")
print(f"star 2 matches found {star2}")
