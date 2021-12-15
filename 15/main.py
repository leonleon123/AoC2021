from numpy import array, zeros
from utils import read_input_lines

data = array(read_input_lines(lambda l: [*l.strip()], __file__, input_file_name='input.txt'), dtype=int)
def adjacent(i, j, shape):
    a, b = shape
    x, y = array([i-1, i+1, i ,i]), array([j, j, j-1, j+1])
    m = (x < 0) | (y < 0) | (x >= a) | (y >= b)
    return [*zip(x[~m], y[~m])]
def shortest_path(mat):
    p = i, j = (0, 0)
    dist = zeros(mat.shape, dtype=int) - 1
    dist[i, j] = 0
    d, q = tuple(array(mat.shape) - 1), [p]
    while p != d:
        p = i, j = q.pop(0)
        for ii, jj in adjacent(i, j, mat.shape):
            if dist[ii, jj] < 0:
                dist[ii, jj] = mat[ii, jj] + dist[i, j]
                q.append((ii, jj))
        q.sort(key=lambda x: dist[x[0], x[1]])
    return dist[-1, -1]
def expanded(mat, k):
    a, b = mat.shape
    d = zeros((a*k, b*k), dtype=int)
    for i in range(k):
        for j in range(k):
            d[i*a:i*a+a, j*b:j*b+b] = mat + i + j
    d[d > 9] = d[d > 9] % 9 
    return d
print(shortest_path(data), shortest_path(expanded(data, 5)), sep='\n')
