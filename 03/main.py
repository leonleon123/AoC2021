from numpy import arange, array, prod, sum
from utils import read_input_lines

data = array(read_input_lines(lambda line: [int(x) for x in line.strip()], __file__))
s = lambda d: (sum(d, axis=0) >= d.shape[0] / 2).astype(int)
p = lambda x, y: prod([b@2**arange(len(b)-1, -1, -1) for b in [x, y]])
f = lambda d, i, n: f(d[d[:, i] == (s(d)^n)[i], :], i+1, n) if d.shape[0] > 1 and i < d.shape[1] else d
print(*[p(x, y) for x,y in [(s(data), s(data)^1), (f(data, 0, 0)[0], f(data, 0, 1)[0])]], sep='\n')
