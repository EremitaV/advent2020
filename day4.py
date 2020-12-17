import re

with open("inputs/day4.txt") as file: 
	pps  = file.read().split("\n\n")

keywords = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
count1 = 0
count2 = 0
for pp in pps:
	if all(x in pp for x in keywords):
		count1 += 1
		#part two 
		fields = pp.split()
		# delete cid from list 
		fields = [x for x in fields if not x.startswith('cid')]
		fields.sort()
		str1 = "".join(fields).strip()		
		rex = "byr:(19[2-9][0-9]|200[0-2])+"\
				 "ecl:(amb|blu|brn|gry|grn|hzl|oth)+"\
				 "eyr:(202[0-9]|2030)+"\
				 "hcl:#([a-z]|[0-9]){6}"\
				 "hgt:((1[5-8][0-9]|19[0-3])+cm|(59|6[0-9]|7[0-6])+in)+"\
				 "iyr:(201[0-9]|2020)+"\
				 "pid:([0-9]){9}$"
		regexp = re.compile(rex)
		if regexp.search(str1):
			count2 += 1
		
print("part one", count1)
print("part two", count2)
