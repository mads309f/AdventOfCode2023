cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
hands = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        (hand, bid) = line.split(' ')
        hands.append((hand, int(bid)))
 

def incScore(s, i):
    return (s * 13 + i)

def HandScore(hand):
    # five of a kind: has same character 5 times
    score = 0

    counts = [hand.count(card) for card in cards]
    # also get index of
    if 5 in counts:
        score = incScore(score, 12)
    elif 4 in counts:
        score = incScore(score, 11)
    elif 3 in counts and 2 in counts:
        score = incScore(score, 10)
    elif 3 in counts:
        score = incScore(score, 9)
    elif counts.count(2) == 2:
        score = incScore(score, 8)
    elif 2 in counts:
        score = incScore(score, 7)

    for c in hand:
        score = incScore(score, cards.index(c))
    return score

scores = [(HandScore(hand), bid) for (hand, bid) in hands]
scores.sort(key=lambda x: x[0])
print(sum([bid * (i+1) for i, (_, bid) in enumerate(scores)]))

