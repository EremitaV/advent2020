with open("inputs/day8.txt") as file: 
	ins  = [x.strip().split(" ") for x in file]

def check(instructions):
	ins = instructions
	ptr = 0
	acc = 0
	visited = set()

	while True: 
		if ptr == len(ins)-1:
			return True, acc
		instr = ins[ptr][0]
		arg = int(ins[ptr][1])
		if ptr in visited:
			return False, acc  
		visited.add(ptr)
		if instr == 'acc':
			acc += arg
			ptr += 1
		elif instr == 'jmp':
			ptr += arg 
		else:
			ptr += 1

print("part one", check(ins)[1])

acc2 = 0
for i in range(len(ins)):
	old = 'nop'
	if ins[i][0] == 'jmp':
		ins[i][0] = 'nop'
		old = 'jmp'
	elif ins[i][0] == 'nop':
		ins[i][0] = 'jmp'
	else: 
		continue
	b,acc = check(ins)
	if b:
		acc2 = acc 
		break
	else: 
		ins[i][0] = old


print("part two", acc2)




