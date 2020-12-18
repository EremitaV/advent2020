with open("inputs/day6.txt") as file: 
	groups  = [x.split("\n") for x in file.read().split("\n\n")]

p1, p2 = 0, 0
for group in groups:
	answers = []
	res = None
	for person in group:
		if person == "": # quick fix . 
			continue
		if res is None: 
			res = set(person)
		else: 
			res = res & set(person)
	str_ = set("".join(group))
	p1 += len(str_)
	p2 += len(res)

print("part one", p1)
print("part two", p2)