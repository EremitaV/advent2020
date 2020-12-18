with open("inputs/day9.txt") as file: 
	nums  = [int(x.strip()) for x in file]

def check(lst, goal):
	for i in range(len(lst)):
		for j in range(len(lst)):
			if lst[i]+lst[j] == goal: 
				return True
	return False

p1 = 0
for i in range(25,len(nums)):
	if not check(nums[i-25:i],nums[i]):
		p1 = nums[i]
		break
print("Part one", p1)

p2 = 0
for i in range(len(nums)):
	sum_ = nums[i]
	for j in range(i+1,len(nums)):
		sum_ += nums[j]
		if sum_ == p1:
			min_ = min(nums[i:j+1])
			max_ = max(nums[i:j+1])
			p2 = min_+max_
			break
		if sum_ > p1:
			continue


print("Part two", p2)