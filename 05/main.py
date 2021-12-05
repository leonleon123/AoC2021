from numpy import abs, arange, array, max, mgrid, reshape, sum, zeros
from utils import read_input_lines

data = array(read_input_lines(lambda *l: array(l).astype(int), __file__, split=r' -> |,'))
d = zeros((2, *max(reshape(data, (data.shape[0]*2, 2))+1, axis=0)), dtype=int)
for [x1,y1,x2,y2] in data:
    sx, sy = 1 if x2 - x1 >= 0 else -1, 1 if y2 - y1 >= 0 else -1
    m = mgrid[x1:x2 + sx:sx, y1:y2 + sy:sy].squeeze().T
    i = m if len(m.shape) == 2 else m[arange(abs(x1-x2)+1), arange(abs(y1-y2)+1)]
    d[:, i[:, 1], i[:, 0]] += 1
    if x1 == x2 or y1 == y2: d[1, i[:, 1], i[:, 0]] += 1
print(sum(d[0] > 1), sum(d[1] > 1), sep='\n')
