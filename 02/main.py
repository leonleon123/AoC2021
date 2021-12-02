import numpy as np

with open('input.txt') as file:
    data = [(s[0], int(s[1])) for x in file.readlines() if (s := x.split(' '))]
pos = np.zeros(5, dtype=int)
dirs = {
    "forward": np.array([   1,  0,  1,  0,  0]),
    "down": np.array([      0,  1,  0,  0,  1]),
    "up": np.array([        0, -1,  0,  0, -1])
}
for d, val in data:
    pos += dirs[d]*val
    pos[3] += dirs[d][0]*val*pos[4]
print(pos[0]*pos[1], pos[2]*pos[3], sep='\n')
