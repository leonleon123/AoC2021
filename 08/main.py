from functools import reduce

from numpy import array, array_split
from utils import read_input_lines

data = read_input_lines(lambda *l: array_split(array([x.strip() for x in l if x]), [10]), __file__, split=r' |\|')
n = {
    (2, 5): '1',
    (0, 2, 5): '7',
    (1, 2, 3, 5): '4',
    (0, 2, 3, 4, 6): '2',
    (0, 2, 3, 4, 5): '3',
    (0, 1, 3, 4, 5): '5',
    (0, 1, 2, 4, 5, 6): '0',
    (0, 1, 3, 4, 5, 6): '6',
    (0, 1, 2, 3, 4, 5): '9',
    (0, 1, 2, 3, 4, 5, 6): '8',
}
n_seg = lambda a, n: [set(x) for x in a if len(x) in n]
and_sets = lambda a: reduce(lambda x, y: x & y, a)
def decode(inp, out):
    c, a = [''] * 7, sorted(inp, key=lambda x: len(x))
    c[0] = (set(a[1]) - set(a[0]) & set(a[1])).pop()
    c[5] = [y for x in n_seg(a, [6]) if len(y := set(x) & set(a[0])) == 1][0].pop()
    c[2] = (set(a[0]) - set(c[5])).pop()
    c[1] = (and_sets(n_seg(a, [6, 4])) - set(c[5])).pop()
    c[3] = (and_sets(n_seg(a, [5, 4])) - set([c[1], c[2], c[5]])).pop()
    c[4] = and_sets([set(x) - set(c) for x in n_seg(a, [6])]).pop()
    c[6] = (set('abcdefg') - set(c)).pop()
    return int("".join([n[tuple(sorted([c.index(y) for y in x]))] for x in out]))
print(sum(sum(len(y) in [2,3,4,7] for y in o) for _, o in data), sum(decode(i, o) for i, o in data), sep='\n')
