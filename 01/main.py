from numpy import diff, sum
from numpy.lib.stride_tricks import sliding_window_view as swv
from utils import read_input

nums = read_input(int, __file__)
print(*[sum(diff(arr) > 0) for arr in [nums, sum(swv(nums, 3), axis=1)]], sep='\n')
