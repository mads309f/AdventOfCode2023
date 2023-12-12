

A = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        sym, nums = line.split(" ")
        nums = [int(i) for i in nums.strip().split(",")]
        A.append((list(sym), nums))

print(len(A))

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

dp = {}
def find_arrangements(num, l_idx, n_idx):
    if (num, l_idx, n_idx) in dp:
        return dp[(num, l_idx, n_idx)]

    line, nums = A[num]
    if n_idx == len(nums):
        if "#" in line[l_idx:]:
            return 0
        return 1

    count = 0
    for i in range(l_idx, len(line)):
        if is_valid(line[i:], nums[n_idx]):
            count += find_arrangements(num, i + nums[n_idx] + 1, n_idx + 1)
        if line[i] == "#":
            break
    dp[(num, l_idx, n_idx)] = count
    return count

for i, e in enumerate(A):
    line, nums = e
    line = ((line + ["?"]) * 5)[:-1]
    nums = nums * 5
    A[i] = (line, nums)

sum = 0
for i in range(len(A)):
    sum += find_arrangements(i, 0, 0)
print(sum)




