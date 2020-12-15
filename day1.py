# Such a small input. Performance doesn't really matter. Might revisit with better implementation. Not likely though.
def part1(input): 
	for i in range(len(input)):
		for j in range(i+1,len(input)):
			if input[i]+input[j] == 2020:
				return input[i]*input[j] 

def part2(input):
	for i in range(len(input)):
		for j in range(i+1,len(input)):
			for k in range(i+2,len(input)):
				if input[i]+input[j]+input[k] == 2020:
					return input[i]*input[j]*input[k] 


with open("inputs/day1.txt") as file: 
	input = [int(line) for line in file]

print(f"part 1: {part1(input)}")
print(f"part 2: {part2(input)}")
