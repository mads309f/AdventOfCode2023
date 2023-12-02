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

        possible = True
        for r in rest:
            num, color = r.split(' ')
            num = int(num)

            if color == 'red' and num > 12:
                possible = False
                break
            elif color == 'green' and num > 13:
                possible = False
                break
            elif color == 'blue' and num > 14:
                possible = False
                break
        
        if possible:
            sum += game_id

print(sum)

                