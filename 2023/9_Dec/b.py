with open("input.txt", "r") as f:
    lines = f.readlines()
    seqs = [list(map(int, line.strip().split(" "))) for line in lines]

def next_seq(lst):
    if all(el == 0 for el in lst):
        return 0
    diff = [lst[i] - lst[i-1] for i in range(1, len(lst))]
    return lst[0] - next_seq(diff)

print(sum([next_seq(seq) for seq in seqs]))
