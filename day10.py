with open("inputs/day10_test2.txt") as file: 
	nums  = [int(x.strip()) for x in file]

nums.sort()
my_adapter = nums[-1]+3

curr = 0
diff = 0 
ones = 0
threes = 1 # our adapter is always 3 higher
for i in nums:
	c_diff = i-curr
	if c_diff == 1:
		ones += 1
	if c_diff == 3:
		threes += 1
	diff += i-curr
	curr = i

print("part one", ones*threes)
curr = 0
diff = 0 
ones = 0
threes = 1 # our adapter is always 3 higher

ways = 1
print(nums)
prev = 1
for i in range(1,len(nums)):
	c_diff = nums[i]-curr
	print(f"nums[i]: {nums[i]}")
	if i+1 < len(nums) and i+2 < len(nums) and i+3 < len(nums):
		if nums[i+3]-nums[i] == 3:
			ways += prev*3
			prev = 3
			continue
	if i+1 < len(nums) and i+2 < len(nums):
		if nums[i+2]-nums[i] <= 3:
		   	ways += prev*2
		   	prev = 2
	prev = 1
	print(f"	ways: {ways}")

print("part two", ways)
#1  3 + 2 + 2 +