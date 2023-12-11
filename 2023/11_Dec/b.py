import numpy as np
# deque
from collections import deque
# priority queue
from queue import PriorityQueue

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
    cols = np.full(A.shape, False)
    rows = np.full(A.shape, False)
    for col in range(A.shape[1]-1, -1, -1):
        # if all zeros
        if np.all(A[:, col] == 0):
            # set column to -1
            cols[:, col] = True
    for row in range(A.shape[0]-1, -1, -1):
        if np.all(A[row, :] == 0):
            # set row to -1
            rows[row, :] = True

print("index: ", index)

def BFS(A, r, c):
    Q = PriorityQueue()

    Q.put((0, r, c, 0))
    while not Q.empty():
        k, r, c, axis = Q.get()
        # print(k, r, c)
        if r < 0 or c < 0 or r >= A.shape[0] or c >= A.shape[1] or A[r, c] != -1:
            continue
        if cols[r, c] and axis == 1:
            k += 1000000 - 1
        if rows[r, c] and axis == 0:
            k += 1000000 - 1

        A[r, c] = k
        Q.put((k+1, r-1, c, 0))
        Q.put((k+1, r+1, c, 0))
        Q.put((k+1, r, c-1, 1))
        Q.put((k+1, r, c+1, 1))


def APSP(A):
    # create b with shape of A and infinity
    B = np.full((index, index), np.inf)

    rows = A.shape[0]
    cols = A.shape[1]
    for r in range(rows):
        for c in range(cols):
            if A[r, c] == 0 or A[r, c] == -1:
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

