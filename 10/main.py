from numpy import median
from utils import read_input_lines

data = read_input_lines(lambda l: l.strip(), __file__)
p = {')': [3, 1], ']': [57, 2], '}': [1197, 3], '>': [25137, 4]}
m = {'(': ')', '[': ']', '{': '}', '<' :'>'}
def errors(line):
    o = []
    for c in line:
        if c in m: o.append(c)
        elif c != m[o.pop()]: return p[c][0], False
    return False, sum(x*5**i for i, x in enumerate(p[m[c]][1] for c in o))
a, b = zip(*[errors(l) for l in data])
print(sum(a), int(median(sorted(x for x in b if x))), sep='\n')
