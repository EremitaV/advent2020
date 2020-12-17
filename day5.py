with open("inputs/day5.txt") as file: 
	board_passes  = [bp.strip() for bp in file]

part1 = 0
nums = []
for bp in board_passes:
	row = range(0,128) # [0,1,...,127]
	for c in bp[:7]:
		if c == 'F':
			row = row[:len(row)//2]
		else:
			row = row[len(row)//2:]
	row = row[0]
	seat = range(0,8) # [0,1,...,7]
	for c in bp[7:]:
		if c == 'L':
			seat = seat[:len(seat)//2]
		else:
			seat = seat[len(seat)//2:]
	seat = seat[0]
	ID = row*8 + seat
	nums.append(ID)
	part1 = max(part1,ID)
	print(f"row {row} seat {seat} ID {ID}")

print("part one", part1)
all_seats = list(range(0,part1))
part2 = max(set(all_seats)-set(nums))
print("part two", part2)