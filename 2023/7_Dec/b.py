cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
hands = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        (hand, bid) = line.split(' ')
        hands.append((hand, int(bid)))
 

def incScore(s, i):
    return s * 13 + i

def HandScore(hand):
    score = 0

    counts = [hand.count(card) for card in cards]
    js, other = counts[0], counts[1:]
    max_c = max(other)
    other.remove(max_c)
    next_max_c = max(other)

    # also get index of
    if max_c + js == 5:
        score = incScore(score, 12)
    elif max_c + js == 4:
        score = incScore(score, 11)
    elif max_c + next_max_c + js == 5:
        score = incScore(score, 10)
    elif max_c + js == 3:
        score = incScore(score, 9)
    elif max_c + next_max_c + js == 4:
        score = incScore(score, 8)
    elif max_c + js == 2:
        score = incScore(score, 7)

    for c in hand:
        score = incScore(score, cards.index(c))
    return score

scores = [(HandScore(hand), bid) for (hand, bid) in hands]
scores.sort(key=lambda x: x[0])
print(sum([bid * (i+1) for i, (_, bid) in enumerate(scores)]))

