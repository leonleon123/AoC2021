from numpy import array, sum, where, zeros
from utils import read_input_lines

d = array(read_input_lines(lambda l: [*l.strip()], __file__), dtype=int)
c, a = zeros(2, dtype=int), d > 9
while not a.all():
    d += 1
    a = m = d > 9
    while (m := d > 9).any():
        a |= m
        for i, j in zip(*where(m)): 
            d[max(i-1, 0):i+2, max(j-1, 0):j+2] += 1
        d[m] = 0
    d[a] = 0
    c += array([sum(a) if c[1] < 100 else 0, 1])
print(*c, sep='\n')
