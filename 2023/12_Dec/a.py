

A = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        sym, nums = line.split(" ")
        nums = [int(i) for i in nums.strip().split(",")]
        A.append((list(sym), nums))

def is_valid(line, num):
    if len(line) < num:
        return False
    for i in range(num):
        if line[i] in ("?", "#"):
            continue
        return False
    if len(line) > num and line[num] == "#":
        return False
    return True

def find_arrangements(line, nums):
    if len(nums) == 0:
        if "#" in line:
            return 0
        return 1
    
    # fit first num 
    count = 0
    for i, ch in enumerate(line):
        if is_valid(line[i:], nums[0]):
            # print(line[i:], nums[0])
            count += find_arrangements(line[i+nums[0]+1:], nums[1:])
        if ch == "#":
            break
    return count

sum = 0
for line, nums in A:
    sum += find_arrangements(line, nums)
print(sum)


