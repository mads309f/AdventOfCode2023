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

# sort map based on source
for m in maps:
    m.sort(key=lambda x: x[1])

# add missing ranges
for m in maps:
    for j in range(1, len(m)):
        end = m[j-1][1] + m[j-1][2]
        if end != m[j][1]:
            m.insert(j, (end, end,  m[j][1] - end))

def get_locations(start, l, depth, i):
    if l <= 0:
        return []
    if depth == len(maps):
        return [start]

    m = maps[depth][i]
    if start + l >= m[1] and start < m[1] + m[2]: 
        return (get_locations(start, min(l, m[1] - start), depth, 0) +
                get_locations(m[0] + abs(start - m[1]), min(l, m[1] + m[2] - start), depth+1, 0) +
                get_locations(m[1] + m[2], start + l - m[1] - m[2], depth, 0))

    if i == len(maps[depth]) - 1:
        return get_locations(start, l, depth+1, 0)

    return get_locations(start, l, depth, i+1)

locations = []
for i in range(0, len(seeds), 2):
    loc = get_locations(seeds[i], seeds[i+1], 0, 0)
    locations.extend(loc)

print(min(locations))
