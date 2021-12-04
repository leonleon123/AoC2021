from numpy import all, any, array, concatenate, sum, where, zeros
from utils import read_input

[p, *b] = read_input(__file__).split('\n\n')
p = array([int(x) for x in p.split(',')])
b = array([[[int(x) for x in l.split(' ') if x] for l in a.split('\n') if l] for a in b])
win = lambda b, a: any(all(b < 0, axis=a)) or any(all(b < 0,axis = a+1))
score = lambda b: ((b + 1).sum() - sum(b != -1)) * num
f, l, wi, won = None, None, None, zeros(b.shape[0]).astype(bool)
for num in p:
    b[b == num] = -1
    wi = where(won == False)[0][0] if sum(~won) == 1 else None
    won[(i := concatenate([where(all(b < 0, axis = a))[0] for a in [1,2]]))] = True
    if l is None and wi is not None and win(b[wi], 0): l = score(b[wi])
    if f is None and win(b, 1): f = score(b[i])
print(f, l, sep='\n')
