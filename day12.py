with open("inputs/day12.txt") as file: 
	directions  = [[line.strip()[:1],line.strip()[1:]] for line in file]

# 	   n,e,s,w 
foo = [0,0,0,0]
current = 1
for direction in directions:
	d = direction[0]
	step = int(direction[1]) 
	if d == 'N': 
		foo[0] += step
	elif d == 'E':
		foo[1] += step
	elif d == 'S':
		foo[2] += step
	elif d == 'W':
		foo[3] += step
	elif d == 'F': 
		foo[current] += step 
	elif d == 'L':
		change = step//90
		current = (current + 4 - change) % 4
	else:
		change = step//90 
		current = (current + change) % 4 

up = max(foo[0],foo[2])-min(foo[0],foo[2])
down = max(foo[1],foo[3])-min(foo[1],foo[3])
res1 = up + down
print("part one", res1)