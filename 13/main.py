from numpy import array_split, flip, max, sum, zeros
from utils import read_input

c, fold = read_input(__file__).split('\n\n')
i, j = zip(*[[int(y) for y in x.split(',')] for x in c.split('\n')])
fold = [x.split(' ')[-1].split('=') for x in fold.split('\n') if x]
m = zeros((max(j)+1, max(i)+1), dtype=int)
m[j, i] = 1
ax, ar = {'y': 0, 'x': 1}, ['.', '#']
for i, [axis, ind] in enumerate(fold):
    a, b = array_split(m, [int(ind)], axis=ax[axis])
    m = a | flip(b[1:] if axis == 'y' else b[:, 1:], axis=ax[axis])
    if i == 0: print(sum(m))
print(*[''.join(ar[y] for y in x) for x in m], sep='\n')
