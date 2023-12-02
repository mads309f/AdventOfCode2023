
sum = 0
# read all lines of a.txt
with open('a.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        # read first and last using while loop
        num = 0
        first = False
        last_num = 0
        for i, c in enumerate(line):
            # if c is digit
            if c.isdigit():
                if not first:
                    num += 10 * int(c)
                    first = True
                last_num = int(c)
        num += last_num
        sum += num

        
                
print(sum)