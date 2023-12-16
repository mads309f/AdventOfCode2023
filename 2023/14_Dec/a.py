
with open("inputc.txt", "r") as f:
    lines = f.readlines()
    rows = len(lines)
    cols = [[] for _ in lines[0]]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in ("O", "#"):
                cols[j].append((c,i))

load = 0
for i, col in enumerate(cols):
    col.sort(key=lambda x: x[1])
    for j, (ch, r) in enumerate(col):
        if ch == "#":
            continue
        if j == 0:
            col[j] = ("O", 0) 
        else:
            col[j] = ("O", col[j-1][1]+1)
        load += rows - col[j][1]

print(load)
