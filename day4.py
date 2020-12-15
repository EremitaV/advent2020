with open("inputs/day4.txt") as file: 
	test  = file.read().split("\n\n")
	input = [line for line in file]

keywords = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
count = 0
for line in test: 
	if all(x in line for x in keywords):
		count += 1 
	
print("part one", count)