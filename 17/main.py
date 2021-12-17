from numpy import array
from utils import read_input

data = read_input(__file__, input_file_name='input.txt')
xa, ya = array([x.split('=')[1].split('..') for x in data.split(': ')[1].split(', ')], dtype=int)

def simulate_throw(v):
    p = array([0, 0])
    v = array(v)
    o = 0
    while p[0] < xa[0] or p[1] > ya[1]:
        p += v
        o = max(p[1], o)
        v -= [int(v[0] > 0), 1]
        if p[0] > xa[1] or p[1] < ya[0]: break
    return p[0] >= xa[0] and p[0] <= xa[1] and p[1] >= ya[0] and p[1] <= ya[1], o

a = [(o, [x, y]) for x in range(500) for y in range(-500, 500) if (o := simulate_throw([x, y]))[0]]
print(max(a, key=lambda x: x[0][1])[0][1], len(set(tuple(x[1]) for x in a)), sep='\n')
