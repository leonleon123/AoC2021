from functools import reduce

from numpy import array, array_split
from utils import read_input_lines

data = read_input_lines(lambda *l: array_split(array([x.strip() for x in l if x]), [10]), __file__, split=r' |\|')
n = {
    (0, 1, 2, 4, 5, 6): '0',
    (2, 5): '1',
    (0, 2, 3, 4, 6): '2',
    (0, 2, 3, 4, 5): '3',
    (1, 2, 3, 5): '4',
    (0, 1, 3, 4, 5): '5',
    (0, 1, 3, 4, 5, 6): '6',
    (0, 2, 5): '7',
    (0, 1, 2, 3, 4, 5, 6): '8',
    (0, 1, 2, 3, 4, 5): '9'
}
out = 0

for s, o in data:
    c = ['']*7
    a = sorted(s, key=lambda x: len(x))
    e = [x for x in a if len(x) in [2,3,4,7]]
    c[0] = (set(e[1])-set(e[0])&set(e[1])).pop()
    c[5] = [y for x in a if len(x) in [6] and len(y := set(x)&set(e[0])) == 1][0].pop()
    c[2] = (set(e[0])-set(c[5])).pop()
    c[1] = (reduce(lambda a, b: a&b, [set(x) for x in a if len(x) in [6, 4]])-set(c[5])).pop()
    c[3] = (reduce(lambda a, b: a&b, [set(x) for x in a if len(x) in [5, 4]])-set([c[1], c[2], c[5]])).pop()
    c[4] = reduce(lambda a, b: a&b, [set(x)-set(c) for x in a if len(x) in [6]]).pop()
    c[6] = (set('abcdefg')-set(c)).pop()
    out += int("".join([n[tuple(sorted([c.index(y) for y in x]))] for x in o]))

print(sum(sum(len(y) in [2,3,4,7] for y in x[1]) for x in data), out, sep='\n')
