from numpy import array
from utils import read_input

t, r = read_input(__file__).split('\n\n')
r = {(y := x.split(' -> '))[0]:y[1] for x in r.split('\n') if x}
def compute_polymer(steps, t, r):
    o, l, c = {t[i:i+2]:t.count(t[i:i+2]) for i in range(len(t)-1)}, t[-2:], {}
    for step in range(steps):
        tmp = {}
        for key in o:
            a, b = key[0]+r[key], r[key]+key[1]
            tmp[a] = o[key] if a not in tmp else tmp[a] + o[key]
            tmp[b] = o[key] if b not in tmp else tmp[b] + o[key]
            if key == l: l = b
        o = tmp
    for key in o: c[key[0]] = o[key] if key[0] not in c else c[key[0]] + o[key]
    c[l[1]] += 1
    return (array(sorted(c[key] for key in c))[[0, -1]] * [-1, 1]).sum()
print(*[compute_polymer(i, t, r) for i in [10, 40]], sep='\n')
