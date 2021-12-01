with open('input.txt') as file:
    nums = [int(x) for x in file.readlines()]
diff = lambda arr: [arr[i+1] - arr[i] for i in range(len(arr)-1)]
sums = [sum(nums[i:i+3]) for i in range(len(nums)-2)]
print(*[sum([x > 0 for x in diff(arr)]) for arr in [nums, sums]], sep='\n')
