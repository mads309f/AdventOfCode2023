
# load input.txt
# init 2d array
with open('input.txt') as f:
    lines = f.readlines()
    len_x = len(lines[0]) - 1
    len_y = len(lines)
    map = [[0 for x in range(len_x)] for y in range(len_y)]

    # load each char into array
    for y in range(len_y):
        for x in range(len_x):
            map[y][x] = lines[y][x]
            
def IsPart(x_s, x_e, row):
    # go through range(x-1, y+1) for
    for x in range(x_s-1, x_e+2):
        for y in range(-1, 2):
            # check out of bounds
            if x < 0 or x >= len_x or y+row < 0 or y+row >= len_y:
                continue
            if map[y+row][x] != '.' and not map[y+row][x].isdigit():
                return True
    return False

def GetNum(x_s, x_e, row):
    num = 0
    for i, x in enumerate(range(x_e, x_s-1, -1)):
        num += int(map[row][x]) * (10 ** i)
    return num

# print(GetNum(5, 7, 0))

sum = 0
for y in range(len_y):
    number_start = -1
    number_end = -1
    for x in range(len_x+1):
        # is digit
        if x != len_x and map[y][x].isdigit():
            if number_start == -1:
                number_start = x
        elif number_start != -1:
            number_end = x-1
            if IsPart(number_start, number_end, y):
                sum += GetNum(number_start, number_end, y)
            
            number_start = number_end = -1
print(sum)