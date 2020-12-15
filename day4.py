with open("inputs/day4.txt") as file: 
	pps  = file.read().split("\n\n")

keywords = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
count = 0
for pp in pps: 
	if all(x in pp for x in keywords):
		count += 1 
	
print("part one", count)