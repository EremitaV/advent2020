with open("inputs/day7.txt") as file: 
	rules  = [x.strip() for x in file]

dict_ = {}
for rule in rules:
	foo = rule.split(" ")
	bags = []
	if "no" in foo:
		pass
	else: 
		for i in range(5,len(foo),4):
			bags.append((foo[i-1],foo[i]+foo[i+1]))
	dict_[foo[0]+foo[1]] = bags

possible_bags = set()
def traverse(outerbag, values):
	for n,v in values: 
		if v == "shinygold":
			possible_bags.add(outerbag)
		traverse(outerbag, dict_[v])


bar = []
# possible_bags.add(new elemnt)
count = 0
for key in dict_: 
	values = dict_[key]
	traverse(key, values)

print("part one", len(possible_bags))


def test2(values):
	res = 1
	for n,v in values:
		res += int(n)*test2(dict_[v])
	return res

print("part two", test2(dict_["shinygold"])-1)