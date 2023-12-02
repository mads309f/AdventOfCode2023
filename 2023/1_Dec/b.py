
# use regex on a.txt
import regex as re
sum = 0
with open('b.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        # find all numbers in line
        numbers = re.findall(r'(?:\d)|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)|(?:ten)', line, overlapped=True)
        # print(numbers)
        # convert all numbers to int
        numbers = [int(n) if n.isdigit() else 1 if n == 'one' else 2 if n == 'two' else 3 if n == 'three' else 4 if n == 'four' else 5 if n == 'five' else 6 if n == 'six' else 7 if n == 'seven' else 8 if n == 'eight' else 9 if n == 'nine' else 10 for n in numbers]
        # sum all numbers
        num = 10 * numbers[0] + numbers[-1]
        sum += num
print(sum)