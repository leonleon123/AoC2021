from numpy import array, zeros
from utils import read_input_lines

dirs = {'f': array([1,  0]),'d': array([0,  1]),'u': array([0, -1])}
data = read_input_lines(lambda d, v: dirs[d[0]]*int(v), __file__, split=' ')
p, d = zeros(2, dtype=int), 0
for dir in data: p, d = p + dir, d + dir[0]*p[1]
print(p[0]*p[1], p[0]*d, sep='\n')
