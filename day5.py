with open("inputs/day5.txt") as file: 
	board_passes  = [bp.strip() for bp in file]

#each letter tells us if we are in higher half or lower half. 

part1 = 0
nums = []
for bp in board_passes:
	row = range(0,128)
	print("bp[:7]", bp[:7])
	for c in bp[:7]:
		print(row)
		if c == 'F':
			row = row[:len(row)//2]
		else:
			row = row[len(row)//2:]
	row = row[0]
	print("row", row)
	seat = range(0,8)
	for c in bp[7:]:
		if c == 'L':
			seat = seat[:len(seat)//2]
		else:
			seat = seat[len(seat)//2:]
	seat = seat[0]
	print("seat", seat)
	ID = row*8 + seat
	nums.append(ID)
	part1 = max(part1,ID)
	print("ID", ID)
print("part one", part1)
all_seats = list(range(0,part1))
part2 = set(all_seats)-set(nums)
print("part two", part2)