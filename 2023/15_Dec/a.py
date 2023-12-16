with open("input.txt") as f:
    strings = f.read().strip().split(",")

def hash(str):
    val = 0
    for s in str:
        val = (val + ord(s)) * 17
    return val & 0xFF

res = 0
for s in strings:
    res += hash(s)
print(res)