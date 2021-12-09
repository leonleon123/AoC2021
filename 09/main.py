from numpy import array, pad, roll, sum
from scipy.ndimage import label
from utils import read_input_lines

d = array(read_input_lines(lambda l: array([*l.strip()], dtype=int), __file__))
d_pad, s = pad(d, ((1,1), (1,1)), constant_values=9), [(0,1), (0,-1), (1, 0), (-1, 0)]
m = array([d_pad < roll(d_pad, axis=(0,1), shift=a) for a in s]).all(axis=0)
l, n = label(d != 9)
print(sum(d_pad[m] + 1), array(sorted(sum(l == x) for x in range(1, n+1))[-3:]).prod(), sep='\n')
