# find lcm of n values
from math import gcd
from functools import reduce
def lcm(xs):
    return reduce(lambda a, b: a * b // gcd(a, b), xs)


graph = {}
with open('input.txt', 'r') as f:
    lines = f.readlines()
    inst = [1 if c == 'R' else 0 for c in lines[0].strip() ]

    for line in lines[2:]:
        label, rest = line.split(' = ')
        r, l = rest.strip()[1:-1].split(',')
        r = r.strip()
        l = l.strip()
        # add key label to graph with value (r, l)
        graph[label] = (r, l)


# select all elements that end with 'A' 
keys = [key for key in graph.keys() if key[-1] == 'A']
loops = []
for i, key in enumerate(keys):
    str = key
    d = 0
    while str[-1] != 'Z':
        str = graph[str][inst[d % len(inst)]]
        d += 1
    loops.append(d)


print(lcm(loops))



# print(keys[0][1])