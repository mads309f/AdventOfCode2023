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


def is_stopped(r, c):
    if r < -2 or r > lr*2 or c < -2 or c > lc*2:
        return True
    elif r % 2 == 1 and c % 2 == 1:
        return False
    elif r % 2 == 1:
        return (is_south(r//2,c//2) and is_north(r//2+1,c//2) and 
               (r//2,c//2) in in_loop and (r//2+1,c//2) in in_loop)
    elif c % 2 == 1:
        return (is_east(r//2,c//2) and is_west(r//2,c//2+1) and 
               (r//2,c//2) in in_loop and (r//2,c//2+1) in in_loop)
    else:
        return (r//2,c//2) in in_loop

outside = set()
q = deque()
q.append((-2,-2))

while len(q) > 0:
    (r, c) = q.popleft()
    if (r,c) in outside or is_stopped(r,c):
        continue
    outside.add((r,c))

    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            q.append((r+dr,c+dc))

visited = set()
for (r,c) in outside:
    if r % 2 == 0 and c % 2 == 0 and not out_of_bounds(r//2,c//2):
        visited.add((r//2,c//2))

inside = lr*lc - len(visited) - len(in_loop)
print(inside)