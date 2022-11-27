
import re
from math import ceil, floor

from utils import read_input_lines


def explode(s: str) -> str:
    c = 0
    for i, ch in enumerate(s):
        c += 1 if ch == '[' else -1 if ch == ']' else 0
        if c == 5:
            l, r = eval(s[i:][:s[i:].find(']')+1])
            li, ri = i, i+s[i:].find(']')+1
            arr = [*s]
            rm = re.match(r'[^\d]*(\d+)', s[ri:])
            if rm:
                rnum = rm.group(1)
                rrs, rre = rm.span(1)
                arr[ri+rrs:ri+rre] = str(int(rnum) + int(r))
            arr[li:ri] = ['0']
            lm = [*re.finditer(r'[^\d]*(\d+)', s[:li])]
            if len(lm):
                lm = lm[-1]
                lnum = lm.group(1)
                lls, lle = lm.span(1)
                arr[lls:lle] = str(int(lnum) + int(l))
            return ''.join(arr)
    return False

def split(s: str) -> str:
    m = re.match(r'.*?(\d\d)', s)
    if m:
        l,r = m.span(1)
        arr = [*s]
        nl, nr =  floor(int(s[l:r]) / 2), ceil(int(s[l:r]) / 2) 
        arr[l:r] = [f'[{nl},{nr}]']
        return ''.join(arr)
    return False

def reduce(s: str) -> str:
    a = s
    while True:
        tmp = explode(a) or split(a)
        if not tmp:
            return a
        a = tmp

def add(a: str, b: str) -> str:
    return reduce(f'[{a},{b}]')

def magnitude(a):
    if isinstance(a, int):
        return a
    l, r = a
    return 3 * magnitude(l) + 2 * magnitude(r)

data = read_input_lines(lambda x: x.replace('\n', ''), __file__, input_file_name='input.txt')

acc = None
for line in data:
    acc = add(acc, line) if acc is not None else line

print(magnitude(eval(acc)))
print(max(magnitude(eval(add(a, b))) for a in data for b in data))