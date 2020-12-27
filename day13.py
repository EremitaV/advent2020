import math

with open("inputs/day13_test.txt") as file: 
	bus  = [line.strip() for line in file]

"""start = int(bus[0])
service = [int(x) for x in bus[1].split(',') if x != 'x']
service2 = [(int(x) if x != 'x' else x) for x in bus[1].split(',')]
print(service2)
min_ = start << 1
id_ = None
for bus in service:
	depart = math.ceil(start/bus)*bus
	if depart < min_: 
		min_ = depart 
		id_ = bus
wait = min_ - start
res1 = id_*wait
print("part one", res1)"""
service2 = [(int(x) if x != 'x' else x) for x in bus[1].split(',')]
service = [int(x) for x in bus[1].split(',') if x != 'x']
max_ = max(service)
min_ = min(service)
print(service)
print(max_)
earliest = 0
found = False
t = 0
while not found:
	if t % 100000 == 0:
		print(t)
	depart = None
	last = None
	diff = 1
	#print(t)
	for i in range(len(service2)):
		if service2[i] == 'x':
			diff += 1
			continue 
		bus = service2[i]
		if depart is not None: 
			if math.ceil(t/bus)*bus == depart + diff:
				depart = depart + diff
				#print("		", depart)
				diff = 1
				if i == len(service2)-1:
					found = True
			else:
				t += max_*min_
				break 
		else:
			depart = math.ceil(t/bus)*bus
			earliest = math.ceil(t/bus)*bus
			#print("		", depart)

print("part two", earliest)
