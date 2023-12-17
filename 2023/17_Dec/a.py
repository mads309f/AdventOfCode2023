
# priority queue
from heapq import heapify, heappush, heappop 

with open("input.txt", "r") as f:
    lines = f.readlines()
    rows = len(lines)
    cols = len(lines[0].strip())
    M = [[int(i) for i in line.strip()] for line in lines]

visited = set()
queue = []
heapify(queue)
heappush(queue, (0, 0, 0, 0, 0, 0)) # cost, r, c, o_dr, o_dc, d

while queue:
    cost, r, c, o_dr, o_dc, d = heappop(queue)

    if (r, c, o_dr, o_dc, d) in visited:
        continue
    if r == rows - 1 and c == cols - 1:
        break
    visited.add((r, c, o_dr, o_dc, d))
    
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        new_d = 1
        nr, nc = r + dr, c + dc
        # out of range
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            continue
        # opposite direction
        if dr == -o_dr and dc == -o_dc:
            continue
        # same direction
        if dr == o_dr and dc == o_dc:
            if d == 3:
                continue
            new_d = d + 1
        heappush(queue, (cost + M[nr][nc], nr, nc, dr, dc, new_d))

print(cost)
