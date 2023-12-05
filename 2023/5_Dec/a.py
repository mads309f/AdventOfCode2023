seeds = []
maps = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = lines[0].split(": ")[1].split(" ")
    seeds = [int(x) for x in seeds]

    for line in lines[1:]:
        # if line contains ':'
        if line.find(":") != -1:
            maps.append([])
        elif line != '\n':
            map = line.strip().split(' ')
            maps[-1].append((int(map[0]), int(map[1]), int(map[2])))

min = -1
for s in seeds:
    for m in maps:
        for i, mapping in enumerate(m):
            if s >= mapping[1] and s < mapping[1] + mapping[2]:
                s = mapping[0] + (s - mapping[1])
                break
    if min == -1 or s < min:
        min = s


print(min)