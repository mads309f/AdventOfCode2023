

with open("input.txt", "r") as f:
    lines = f.readlines()
    rows = len(lines)
    cols = len(lines[0].strip())
    col_list = [[] for _ in range(cols)]
    for r, line in enumerate(lines):
        for c, sym in enumerate(line.strip()):
            if sym in ("O", "#"):
                col_list[c].append((sym, r))


def print_cols(transpose=False):
    syms = []
    poses = []
    for i in range(len(col_list)):
        if len(col_list[i]) == 0:
            continue
        sym, pos = zip(*col_list[i])
        syms += sym
        if transpose:
            poses += list(zip([i]*len(pos), pos))
        else:
            poses += list(zip(pos, [i]*len(pos)))
    for i in range(rows):
        for j in range(cols):
            if (i, j) in poses:
                print(syms[poses.index((i, j))], end="")
            else:
                print(".", end="")
        print()

def do_cycle():
    global col_list
    temp = [[] for _ in range(rows)]
    curr = col_list
    for it in range(4):
        for i, lst in enumerate(curr): # i = column
            if it in (0, 1):
                lst = sorted(lst, key=lambda x: x[1])
            else:
                lst = sorted(lst, key=lambda x: x[1], reverse=True)
            for j, (sym, k) in enumerate(lst): # k = row
                if sym == '#':
                    temp[k].append((sym, i))
                else:
                    if it in (0, 1):
                        new_index = lst[j-1][1]+1 if j != 0 else 0
                    else:
                        new_index = lst[j-1][1]-1 if j != 0 else len(temp)-1
                    temp[new_index].append((sym, i))
                    lst[j] = (sym, new_index)
        curr, temp = temp, [[] for _ in range(len(curr))]
        col_list = curr


def calculate_load():
    load = 0
    for i, col in enumerate(col_list):
        for j, (ch, r) in enumerate(col):
            if ch == "#":
                continue
            load += rows - col[j][1]
    return load

state = []
goal = 1000000000
cycle_start = 500
for i in range(1, goal+1):
    do_cycle()
    # lets try to find cycle after 500 iterations
    if i == cycle_start:
        state = [l.copy() for l in col_list]
    elif col_list == state:
        print("cycle found with len: ", i - cycle_start)
        cycles_more = (goal - cycle_start) % (i - cycle_start)
        for _ in range(cycles_more):
            do_cycle()
        print("load: ", calculate_load())
        
        break
        