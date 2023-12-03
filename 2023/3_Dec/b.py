

# load input.txt
with open('input.txt') as f:
    lines = f.readlines()
    len_x = len(lines[0]) - 1
    len_y = len(lines)
    map = [[0 for x in range(len_x)] for y in range(len_y)]

    # load each char into array
    for y in range(len_y):
        for x in range(len_x):
            # insert 
            map[y][x] = lines[y][x]

def GetNum(x_s, x_e, row):
    num = 0
    for i, x in enumerate(range(x_e-1, x_s-1, -1)):
        num += int(map[row][x]) * (10 ** i)
    return num

def ComputeGearRatio(x_s, x_e, row):
    # go through range(x-1, y+1) for
    for x in range(x_s-1, x_e+1):
        for y in range(-1, 2):
            # check out of bounds
            if x < 0 or x >= len_x or y+row < 0 or y+row >= len_y:
                continue
            elif map[y+row][x][0] == '*':
                num = GetNum(x_s, x_e, row)
                curr = map[y+row][x][1:]
                if curr == '':
                    map[y+row][x] = f"*{num}"
                    curr = 0

                return num * int(curr)
    return 0

sum = 0
for y in range(len_y):
    number_start = -1
    for x in range(len_x+1):
        if x != len_x and map[y][x].isdigit():
            if number_start == -1:
                number_start = x
        elif number_start != -1:
            sum += ComputeGearRatio(number_start, x, y)
            number_start = -1
print(sum)