with open("input.txt") as f:
    strings = f.read().strip().split(",")

def hash(str):
    val = 0
    for s in str:
        val = (val + ord(s)) * 17
    return val & 0xFF

hashmap = [[] for _ in range(256)]

def update_lst(label, val):
    
    h = hash(label)
    for i, (l, _) in enumerate(hashmap[h]):
        if l == label:
            if val is None:
                del hashmap[h][i]
            else:
                hashmap[h][i] = (l, val)
            return
    if val is not None:
        hashmap[h].append((label, val))


for s in strings:
    if "=" in s:
        update_lst(*s.split("="))
    else:
        update_lst(s[:-1], None)

res = 0
for i, h in enumerate(hashmap):
    for j, (_, val) in enumerate(h):
        res += (i+1) * (j+1) * int(val)
print(res)