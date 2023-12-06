
with open('input.txt', 'r') as f:
    lines = f.readlines()
    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

def binSearch(time, dist, predicate):
    left = 0
    right = time
    while left < right:
        mid = (left + right) // 2
        moved = mid * (time - mid)
        if predicate(moved, dist):
            right = mid
        else:
            left = mid + 1
    return left

res = (binSearch(time, dist, lambda m, d: m < d) - 
       binSearch(time, dist, lambda m, d: m >= d))

print(res)