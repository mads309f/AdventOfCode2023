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

# sort based on mapping[1]
for m in maps:
    m.sort(key=lambda x: x[1])

# add missing ranges
for m in maps:
    for j in range(len(m)):
        if j == 0:
            continue
        if m[j-1][1] + m[j-1][2] != m[j][1]:
            m_len = m[j][1] - (m[j-1][1] + m[j-1][2])
            m.insert(j, (m[j-1][1] + m[j-1][2], m[j-1][1] + m[j-1][2], m_len))

def get_locations(start, l, mi):
    if l <= 0:
        return []
    if mi == len(maps):
        return [(start, l)]
    locs = []
    for m in maps[mi]:

        if start <= m[1] and start + l > m[1]: 
            # call get_locations 3 times
            
            locs.extend(
                get_locations(start, min(l, m[1] - start), mi) +
                get_locations(m[0] + m[1] - start, min(l, m[1] + m[2] - start), mi+1) +
                get_locations(m[1] + m[2], start + l - m[1] - m[2], mi)
            )

            return locs

        if start > m[1] and start < m[1] + m[2]: 
            locs.extend(
                get_locations(m[0] + start - m[1], min(l, m[1] + m[2] - start), mi+1) +
                get_locations(m[1] + m[2], start + l - m[1] - m[2], mi)
            )
            return locs

    locs.extend(get_locations(start, l, mi+1))
    return locs

locations = []
for i in range(0, len(seeds), 2):
    loc = get_locations(seeds[i], seeds[i+1], 0)
    locations.extend(loc)


min = -1
for l in locations:
    if min == -1 or l[0] < min:
        min = l[0]
print(min)
