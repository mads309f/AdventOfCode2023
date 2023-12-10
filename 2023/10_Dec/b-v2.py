from collections import deque

with open("input.txt", "r") as f:
    lines = f.readlines()
    pipes = []
    for line in lines:
        pipes.append(list(line.strip()))
    lr = len(pipes)
    lc = len(pipes[0]) 
    for i, row in enumerate(pipes):
        for j, c in enumerate(row):
            if c == 'S':
                s = (i, j)

def out_of_bounds(r, c):
    return r < 0 or r >= lr or c < 0 or c >= lc

def is_east(r, c):
    return not out_of_bounds(r, c) and pipes[r][c] in ('-','L','F','S')
def is_west(r, c):
    return not out_of_bounds(r, c)and pipes[r][c] in ('-','J','7','S')
def is_south(r, c):
    return not out_of_bounds(r, c) and pipes[r][c] in ('|','7','F','S')
def is_north(r, c):
    return not out_of_bounds(r, c) and pipes[r][c] in ('|','L','J','S')

def find_longest(r, c, pr, pc):
    if out_of_bounds(r, c):
        return set()
    in_loop = set()
    d = 1
    while pipes[r][c] != 'S':
        in_loop.add((r,c))
        if c-1 != pc and is_east(r, c-1) and is_west(r, c): # check west
            (pr, pc) = (r, c)
            c -= 1
        elif c+1 != pc and is_west(r, c+1) and is_east(r, c): # east
            (pr, pc) = (r, c)
            c += 1
        elif r-1 != pr and is_south(r-1, c) and is_north(r, c): # north
            (pr, pc) = (r, c)
            r -= 1
        elif r+1 != pr and is_north(r+1, c) and is_south(r, c): # south
            (pr, pc) = (r, c)
            r += 1
        else:
            return set()
        d += 1
    
    in_loop.add((r,c))
    return in_loop

in_loop = set()
for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
    new_loop = find_longest(s[0]+dr, s[1]+dc, s[0], s[1])
    if len(new_loop) > len(in_loop):
        in_loop = new_loop

nlc, nlr = lc*2+1, lr*2+1
new_map = [[False for _ in range(nlc)] for _ in range(nlr)]

def create_map(r, c):
    dr, dc = r*2+1, c*2+1
    new_map[dr][dc] = True
    if pipes[r][c] == 'S':
        return
    if dc+1 < nlc:
        new_map[dr][dc+1] = is_east(r, c)
    if dc-1 >= 0:
        new_map[dr][dc-1] = is_west(r, c)
    if dr+1 < nlr:
        new_map[dr+1][dc] = is_south(r, c)
    if dr-1 >= 0:
        new_map[dr-1][dc] = is_north(r, c)

for r, c in in_loop:
    create_map(r, c)

def is_visited(r, c):
    return r < 0 or r >= nlr or c < 0 or c >= nlc or new_map[r][c]

# dfs
q = deque()
q.append((0,0))
while len(q) > 0:
    r, c = q.pop()
    if is_visited(r, c):
        continue
    new_map[r][c] = True
    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
        q.append((r+dr,c+dc))

count = 0
for r in range(1, nlr, 2):
    for c in range(1, nlc, 2):
        if not new_map[r][c]:
            count += 1
print(count)
