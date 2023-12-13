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
def find_mirror(M, axis):
    n = M.shape[axis]
    for j in range(n-1):
        k_len = min(j+1, n-j-1)
        for k in range(k_len):
            if axis == 0:
                diff = np.sum(M[j-k, :] != M[j+k+1, :])
            else:
                diff = np.sum(M[:, j-k] != M[:, j+k+1])
            if diff > 0:
                break   
            if k == k_len-1:
                return 100*(j+1) if axis == 0 else j+1
    return 0

sum = 0
for m in M:
    sum += find_mirror(np.array(m), 0) + find_mirror(np.array(m), 1)
print(sum)
                