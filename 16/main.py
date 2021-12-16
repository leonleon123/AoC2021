from numpy import arange, array, array_split, concatenate, prod
from utils import read_input

to_int = lambda arr: arr@2**arange(len(arr) - 1, -1, -1)

def parse_packet(b):
    V, T, rest = array_split(b, [3, 6])
    v, t = to_int(V), to_int(T)
    if t != 4:
        I, rest = array_split(rest, [1])
        i = I[0]
        L, rest = array_split(rest, [11 if i else 15])
        l = to_int(L)
        r = array([0, 0])
        sub = []
        while r[i] < l:
            tmp, rest = parse_packet(rest)
            r += [tmp[-1], 1]
            sub.append(tmp)
        return (v, t, sub, 6+1+len(L)+r[0]), rest
    else:
        A, rest = array_split(rest, [5])
        n = A[1:]
        while A[0]:
            A, rest = array_split(rest, [5])
            n = concatenate((n, A[1:]))
        return (v, t, to_int(n), 6+len(n)+len(n)//4), rest
        
def add_v(p):
    return p[0] + (sum(add_v(x) for x in p[2]) if p[1] != 4 else 0)

def evaluate_packets(p):
    if p[1] == 0:   return sum(evaluate_packets(x) for x in p[2])
    elif p[1] == 1: return prod([evaluate_packets(x) for x in p[2]])
    elif p[1] == 2: return min(evaluate_packets(x) for x in p[2])
    elif p[1] == 3: return max(evaluate_packets(x) for x in p[2])
    elif p[1] == 4: return p[2]
    elif p[1] == 5: return int(evaluate_packets(p[2][0]) > evaluate_packets(p[2][1]))
    elif p[1] == 6: return int(evaluate_packets(p[2][0]) < evaluate_packets(p[2][1]))
    elif p[1] == 7: return int(evaluate_packets(p[2][0]) == evaluate_packets(p[2][1]))

data = read_input(__file__)
bin_str = "".join([f"{bin(int(x.strip(), 16))[2:]:0>4}" for x in data if x.strip()])
b = array([*bin_str], dtype=int)
p, rest = parse_packet(b)
print(add_v(p), evaluate_packets(p), sep='\n')
