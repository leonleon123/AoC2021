from numpy import array, diff, sum
from numpy.lib.stride_tricks import sliding_window_view as swv

with open('input.txt') as file:
    nums = array([int(x) for x in file.readlines()])
print(*[sum(diff(arr) > 0) for arr in [nums, sum(swv(nums, 3), axis=1)]], sep='\n')
