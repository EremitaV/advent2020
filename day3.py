with open("inputs/day3.txt") as file: 
	input = [line.rstrip() for line in file]

width = len(input[0]) # used to determine when the pattern repeats.
height = len(input)

def traverse(right, down):
	step, tree_count = 0, 0
	for i in range(down,height,down):
		step = (step + right) % width
		if input[i][step] == '#':
			tree_count += 1 
	return tree_count

print("part one:",traverse(3,1))

res2 = traverse(1,1)*traverse(3,1)*traverse(5,1)*traverse(7,1)*traverse(1,2)
print("part two:",res2)
