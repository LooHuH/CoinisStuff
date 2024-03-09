from askvar import askvar

nums = [askvar(f'num {x+1}') for x in range(3)]
sums = [nums[x] + nums[x-1] for x in range(len(nums))]
print(f'Cheapest sum of two - {min(sums)}')