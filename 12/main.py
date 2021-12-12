from utils import read_input_lines

data = read_input_lines(lambda a, b: (a.strip(), b.strip()), __file__, split='-')
d = [*data, *[(y,x) for x,y in data]]
c = {a: [y for x, y in d if x == a] for a, b in d}
def find_paths(i, v, n):
    s = [v.count(x) for x in set(v) if x.lower() == x and x not in ['start', 'end']]
    if (n > 1 and s.count(n) > 1) or any(x > n for x in s): return 0
    if i == 'end': return 1
    return sum(find_paths(x, [*v, x], n) for x in c[i] if x != 'start')
print(*[find_paths('start', ['start'], i) for i in range(1,3)], sep='\n')
