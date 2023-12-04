
cards = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        
        winning, have = line.split(':')[1].strip().split(' | ')
        winning = winning.strip().split(' ')
        have = have.strip().split(' ')
        # remove empty strings
        winning = [int(x) for x in winning if x]
        have = [int(x) for x in have if x]

        matches = 0
        for card in have:
            if card in winning:
                matches += 1

        # append to cards
        cards.append(matches)

# ** It is a DP problem - either use top down or bottom up**
# Top down DP
dp = [-1] * len(cards)
def get_score(i):
    if dp[i] != -1:
        return dp[i]
    score = 1
    for j in range(i+1, i+1+cards[i]):
        score += get_score(j)
    dp[i] = score
    return score

score = 0
for i in range(len(cards)):
    score += get_score(i)
print(score)

# Bottom up DP
score = [-1] * len(cards)
for i in range(len(cards)-1, -1, -1):
    score[i] = 1
    for j in range(i+1, i+1+cards[i]):
        score[i] += score[j]
print(sum(score))