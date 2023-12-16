with open('input.txt') as f:
    chars = [list(line.strip()) for line in f.readlines()]
    rows = len(chars)
    cols = len(chars[0])


visited = set()
queue = [(0, 0, 0, 1)]
cells = 0
while queue:
    r, c, dr, dc = queue.pop(0)
    if r < 0 or r >= rows or c < 0 or c >= cols or (r, c, dr, dc) in visited:
        continue
    visited.add((r, c, dr, dc))

    if chars[r][c] == '.':
        queue.append((r+dr, c+dc, dr, dc))
    elif chars[r][c] == '\\':
        n_dr, n_dc = dc, dr
        queue.append((r+n_dr, c+n_dc, n_dr, n_dc))
    elif chars[r][c] == '/':
        n_dr, n_dc = -dc, -dr
        queue.append((r+n_dr, c+n_dc, n_dr, n_dc))
    elif chars[r][c] == '-':
        if dr == 0:
            queue.append((r+dr, c+dc, dr, dc))
        else:
            queue.append((r, c+1, 0, 1))
            queue.append((r, c-1, 0, -1))
    elif chars[r][c] == '|':
        if dc == 0:
            queue.append((r+dr, c+dc, dr, dc))
        else:
            queue.append((r+1, c, 1, 0))
            queue.append((r-1, c, -1, 0))

cells = 0
for i in range(rows):
    for j in range(cols):
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (i, j, dr, dc) in visited:
                cells += 1
                break
print(cells)

# for i in range(rows):
#     for j in range(cols):
#         draw = False
#         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             if (i, j, dr, dc) in visited:
#                 print('#', end='')
#                 draw = True
#                 break
#         if not draw:
#             print(".", end='')
#     print()
                