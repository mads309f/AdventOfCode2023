import numpy as np
# deque
from collections import deque

index = 0
def parse(x):
    global index
    if x == '.':
        return 0
    else:
        index += 1
        return index

with open('input.txt') as f:
    chars = [list(map(parse, line.strip())) for line in f.readlines()]
    A = np.array(chars)
    for col in range(A.shape[1]-1, -1, -1):
        # if all zeros
        if np.all(A[:, col] == 0):
            A = np.insert(A, col, 0, axis=1)
    for row in range(A.shape[0]-1, -1, -1):
        if np.all(A[row, :] == 0):
            A = np.insert(A, row, 0, axis=0)

print("index: ", index)

def BFS(A, r, c):
    # if out of bounds
    Q = deque()
    Q.append((r, c, 0))
    while len(Q) > 0:
        r, c, k = Q.popleft()
        if r < 0 or c < 0 or r >= A.shape[0] or c >= A.shape[1] or A[r, c] != -1:
            continue
        A[r, c] = k
        Q.append((r-1, c, k+1))
        Q.append((r+1, c, k+1))
        Q.append((r, c-1, k+1))
        Q.append((r, c+1, k+1))


def APSP(A):
    # create b with shape of A and infinity
    B = np.full((index, index), np.inf)

    rows = A.shape[0]
    cols = A.shape[1]
    for r in range(rows):
        for c in range(cols):
            if A[r, c] == 0:
                continue
            print(A[r, c])
            C = np.full(A.shape, -1)
            BFS(C, r, c)
            for rr in range(rows):
                for cc in range(cols):
                    if A[rr, cc] == 0:
                        continue
                    B[A[r, c]-1, A[rr, cc]-1] = C[rr, cc]
    return B


B = APSP(A)
# sum upper triangle
print(np.sum(np.triu(B)))

