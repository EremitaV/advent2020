with open("inputs/day11.txt") as file: 
	seats  = [list(line.strip()) for line in file]

def save_current_state(grid):
	return [row[:] for row in grid]

# 1 2 3
# 4 5 6
# 7 8 9
def adj(grid,x_cord,y_cord, copy):
	# general case
	count = 0 
	dots = 0
	occupied = 0
	#print(f"checking ({x_cord},{y_cord})")
	for row in range(-1+x_cord,2+x_cord):
		if row < 0: 
			continue
		for col in range(-1+y_cord,2+y_cord):
			#print(f"	row {row} col {col}")
			if len(grid) > row >= 0 and len(grid[0]) > col >= 0:
				#print(f"checking row: {row} and col {col}")
				if row == x_cord and col == y_cord:
					continue
				if grid[row][col] == 'L':
					count += 1
				if grid[row][col] == '.':
					dots += 1
				if grid[row][col] == '#':
					occupied += 1
	#print(f"		dots {dots} count {count} sum = {dots+count}")
	if grid[x_cord][y_cord] == 'L':
		if dots + count == 8:
			copy[x_cord][y_cord] = '#'
		# checking first and last row 	
		if (x_cord == 0 or x_cord == len(grid)-1) and (dots + count == 5):
			copy[x_cord][y_cord] = '#'
		# check first and last column 
		if (y_cord == 0 or y_cord == len(grid[0])-1) and (dots + count == 5):
			copy[x_cord][y_cord] = '#'
		# checking corners
		if y_cord == 0 and x_cord == 0 and (dots + count == 3):
			copy[x_cord][y_cord] = '#'
		if y_cord == 0 and x_cord == len(grid)-1 and (dots + count == 3):
			copy[x_cord][y_cord] = '#'
		if y_cord == len(grid[0])-1 and x_cord == 0 and (dots + count == 3):
			copy[x_cord][y_cord] = '#'
		if y_cord == len(grid[0])-1 and x_cord == len(grid)-1 and (dots + count == 3):
			copy[x_cord][y_cord] = '#'
	if grid[x_cord][y_cord] == '#': 
		#print("HERE")
		if occupied >= 4: 
			#print(f"	occupied {occupied}")
			copy[x_cord][y_cord] = 'L'
	# edge case 
	return copy

copy = save_current_state(seats)
current = save_current_state(seats)
changed = False
def check_equal(first, second):
	for i in range(len(first)):
		str1 = "".join(first[i])
		str2 = "".join(second[i])
		if str1 != str2:
			return False
	return True

def count_occupied(grid):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '#':
				count += 1
	return count

while not changed:
	#print("INPUT")
	#for cur in current: 
	#	print(cur)
	for x in range(len(current)):
		for y in range(len(current[0])):
			copy = adj(current,x,y,copy)
	#print("OUTPUT")
	#for c in copy: 
	#	print(c)
	#print(25*"*")
	#print(f"equal after {i+1} rounds? {check_equal(current,copy)}")
	changed = check_equal(current,copy)
	current = save_current_state(copy)
	copy = save_current_state(copy)

part1 = count_occupied(copy)
print(f"part one {part1}")
#while not changed:
#	for x in range(len(current)):
#		for y in range(len(seats[0])):
#			copy = adj(seats,x,y,copy)


#for s in seats: 
#	print(s)
#print(20*"*")


# rules are applied simultaneously
# 1: If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# 2: If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# 3: Otherwise, the seat's state does not change.
# floor (.) never changes. 
#for seat in seats: 
#	print(seat)


