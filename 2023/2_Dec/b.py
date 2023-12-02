sum = 0
#  read lines of input.txt
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        id, rest = line.split(':')
        game_id = int(id.split(' ')[1])
        # split rest at ';' and ','
        rest = rest.split(';')
        rest = [x.split(',') for x in rest]
        # 2 dim to 1 dim
        rest = [item.strip() for sublist in rest for item in sublist]

        max_red = 0
        max_green = 0
        max_blue = 0
        for r in rest:
            num, color = r.split(' ')
            num = int(num)

            if color == 'red' and num > max_red:
                max_red = num
            elif color == 'green' and num > max_green:
                max_green = num
            elif color == 'blue' and num > max_blue:
                max_blue = num
        
        sum += max_red * max_green * max_blue

print(sum)

                