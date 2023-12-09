# create hashset
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

print(inst)
print(graph)

str = 'AAA'
d = 0
while str != 'ZZZ':
    str = graph[str][inst[d % len(inst)]]
    # print(str)
    d += 1


print(d)