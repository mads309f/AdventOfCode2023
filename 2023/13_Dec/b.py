import numpy as np

M = []
with open("input.txt") as f:
    lines = f.readlines()
    m = []
    for line in lines:
        if line == "\n":
            M.append(m)
            m = []
            # break # delete
        else:
            m.append(list(line.strip()))
    M.append(m)


# handle rows
def find_mirror(M, mul):
    axis = 0
    n = M.shape[axis]
    for j in range(n-1):
        k_len = min(j+1, n-j-1)
        smudge = False
        for k in range(k_len):
            diff = np.sum(M[j-k, :] != M[j+k+1, :])
            if diff == 1 and not smudge:
                smudge = True
            elif diff > 0:
                break   
            if k == k_len-1 and smudge:
                return mul*(j+1)
    return 0

sum = 0
for m in M:
    sum += (find_mirror(np.array(m), 100) + 
            find_mirror(np.transpose(np.array(m)), 1))
print(sum)
                