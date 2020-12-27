with open("inputs/day14.txt") as file: 
	input_  = [line.strip().split('=') for line in file]

mem_dict = {}
mask = None
for inp in input_:
	if inp[0].strip() == "mask":
		mask = inp[1].strip()
	else: 
		mem = inp[0]
		mem = mem.split('[')
		memloc = int(mem[1][0:len(mem[1])-2])
		number = bin(int(inp[1],10))
		z = 36*"0"
		z = z[len(number[2:]):]+number[2:]
		str_build = ""
		for i,j in zip(z,mask):
			if j == '0':
				str_build += j
			elif j == '1':
				str_build += j
			else:
				str_build += i
		res = int(str_build,2)
		mem_dict[memloc] = res

res = sum(mem_dict.values())
print("part one",res)
mask = None
mem_dict2 = {}
for inp in input_:
	if inp[0].strip() == "mask":
		mask = inp[1].strip()
	else: 
		mem = inp[0]
		mem = mem.split('[')
		memloc = bin(int(mem[1][0:len(mem[1])-2]))
		number = int(inp[1],10)
		z = 36*"0"
		z = z[len(memloc[2:]):]+memloc[2:]
		str_build = [""]
		for i,j in zip(z,mask):
			if j == '0':
				for ind in range(len(str_build)):
					str_build[ind] += i # keep bit from original address 
			elif j == '1':
				for ind in range(len(str_build)):
					str_build[ind] += j
			else: # j == 'X'
				for ind in range(len(str_build)):
					str_ = str_build[ind]
					str_build[ind] = str_+'0'
					str_build.append(str_+'1')

		for meml in str_build:
			addr = int(meml,2)
			#print("		writing to address", addr)
			mem_dict2[addr] = number

res2 = sum(mem_dict2.values())
print("part two", res2)