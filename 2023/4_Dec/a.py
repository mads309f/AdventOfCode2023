

sum = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        
        winning, have = line.split(':')[1].strip().split(' | ')
        winning = winning.strip().split(' ')
        have = have.strip().split(' ')
        # remove empty strings
        winning = [int(x) for x in winning if x]
        have = [int(x) for x in have if x]

        score = 0
        for card in have:
            if card in winning:
                score = 1 if score == 0 else score * 2
        sum += score

print(sum)
        