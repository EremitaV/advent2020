with open("inputs/day12.txt") as file: 
	directions  = [[line.strip()[:1],line.strip()[1:]] for line in file]

# 	   n,e,s,w 
foo = [0,0,0,0]	# ship position compared to start position
foo2 = [0,0,0,0]
wp = [1,10,0,0] # waypoint 
print([sum(x) for x in zip(foo,wp)])
current = 1
for direction in directions:
	d = direction[0]
	step = int(direction[1]) 
	if d == 'N': 
		# TODO: instead of list of all directions just move up/down and left/right 
		# keeping track of just two variables. 
		foo[0] += step
		wp[0] += step
	elif d == 'E':
		foo[1] += step
		wp[1] += step
	elif d == 'S':
		foo[2] += step
		wp[2] += step
	elif d == 'W':
		foo[3] += step
		wp[3] += step
	elif d == 'F': 
		foo[current] += step 
		#part two 
		foo2[0] += step*wp[0]
		foo2[1] += step*wp[1]
		foo2[2] += step*wp[2]
		foo2[3] += step*wp[3] 
	elif d == 'L':
		#part one 
		change = step//90
		current = (current + 4 - change) % 4
		#part two 
		d0, d1, d2, d3 = wp[0], wp[1], wp[2], wp[3]
		wp0 = (0 + 4 - change) % 4
		wp1 = (1 + 4 - change) % 4
		wp2 = (2 + 4 - change) % 4
		wp3 = (3 + 4 - change) % 4
		wp[wp0], wp[wp1], wp[wp2], wp[wp3] = d0, d1, d2, d3

	else:
		#part one 
		change = step//90 
		current = (current + change) % 4 
		#part two
		d0, d1, d2, d3 = wp[0], wp[1], wp[2], wp[3]
		wp0 = (0 + change) % 4
		wp1 = (1 + change) % 4
		wp2 = (2 + change) % 4
		wp3 = (3 + change) % 4
		wp[wp0], wp[wp1], wp[wp2], wp[wp3] = d0, d1, d2, d3 

up = max(foo[0],foo[2])-min(foo[0],foo[2])
down = max(foo[1],foo[3])-min(foo[1],foo[3])
res1 = up + down

up2 = max(foo2[0],foo2[2])-min(foo2[0],foo2[2])
down2 = max(foo2[1],foo2[3])-min(foo2[1],foo2[3])

res2 = up2 + down2
print("part one", res1)
print("part two", res2)
