from numpy import abs, array, max, median, mgrid, min, sum
from utils import read_input_lines

d = read_input_lines(lambda *l: array(l, dtype=int), __file__, split=',')[0]
print(sum(abs(d - median(d)), dtype=int))
print(min(sum(((n := abs(mgrid[0:max(d)+1, 0:len(d)][0]-d))*(n+1))/2, axis=1, dtype=int)))
