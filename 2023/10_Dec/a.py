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

def find_longest(r, c, pr, pc, d):
    if pipes[r][c] == 'S' and d > 0:
        return d
    res = -1
    if c > 0 and c-1 != pc and pipes[r][c-1] in ('-','L','F','S'): # west
        res = max(res, find_longest(r, c-1, r, c, d+1))

    if c < lc-1 and c+1 != pc and pipes[r][c+1] in ('-','J','7','S'): # east
        res = max(res, find_longest(r, c+1, r, c, d+1))

    if r > 0 and r-1 != pr and pipes[r-1][c] in ('|','7','F','S'): # north
        res = max(res, find_longest(r-1, c, r, c, d+1))

    if r < lr-1 and r+1 != pr and pipes[r+1][c] in ('|','L','J','S'): # south
        res = max(res, find_longest(r+1, c, r, c, d+1))

    return res

def is_east(r, c):
    return c >= 0 and c < lc and pipes[r][c] in ('-','L','F','S')
def is_west(r, c):
    return c >= 0 and c < lc and pipes[r][c] in ('-','J','7','S')
def is_south(r, c):
    return r >= 0 and r < lr and pipes[r][c] in ('|','7','F','S')
def is_north(r, c):
    return r >= 0 and r < lr and pipes[r][c] in ('|','L','J','S')

def find_longest(r, c, pr, pc):

    d = 1
    while pipes[r][c] != 'S':
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
            return -1
        d += 1
            
    return d

res = -1
if is_east(s[0], s[1]-1):
    res = max(res, find_longest(s[0], s[1]-1, s[0], s[1]))
if is_west(s[0], s[1]+1):
    res = max(res, find_longest(s[0], s[1]+1, s[0], s[1]))
if is_south(s[0]-1, s[1]):
    res = max(res, find_longest(s[0]-1, s[1], s[0], s[1]))
if is_north(s[0]+1, s[1]):
    res = max(res, find_longest(s[0]+1, s[1], s[0], s[1]))


dist = int((res + 0.5) * 0.5)
print(dist)