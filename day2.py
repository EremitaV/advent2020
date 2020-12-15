with open("inputs/day2.txt") as file: 
	input = [line.split(" ") for line in file]

def getbounds(bounds):
	bounds = bounds.split("-")
	return int(bounds[0]),int(bounds[1])
 
def check(condition1, condition2):
	correct1, correct2 = 0, 0
	for i in range(len(input)):
		l,h = getbounds(input[i][0])
		letter = input[i][1][0]
		password = input[i][2]
		count = password.count(letter)
		first = password[l-1] == letter
		second = password[h-1] == letter
		if eval(condition1): 
			correct1 += 1 # l <= count <= h
		if eval(condition2): # first ^ second XOR 
			correct2 += 1
	return correct1, correct2

res1, res2 = check("l <= count <= h","first ^ second")


print("Part one", res1)
print("Part two", res2)