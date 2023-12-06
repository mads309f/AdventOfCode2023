
with open('input.txt', 'r') as f:
    lines = f.readlines()
    times = lines[0].split(":")[1].split(" ")
    times = [int(x) for x in times if x]
    dists = lines[1].split(":")[1].split(" ")
    dists = [int(x) for x in dists if x]

mul = 1
for t, d in zip(times, dists):
    pos = 0
    for i in range(t):
        moved = i * (t - i)
        if moved >= d:
            pos += 1
    mul *= pos
print(mul)