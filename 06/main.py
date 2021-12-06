from numpy import array, eye, roll, sum
from utils import read_input_lines

data = read_input_lines(lambda *l: array(l, dtype=int), __file__, split=',')[0]
f = lambda i, c: sum(c) if i == 0 else f(i-1, roll(c+eye(9, dtype=int)[7]*c[0], -1))
print(f(80, (c := array([sum(data == x) for x in range(9)]))), f(256, c), sep='\n')
