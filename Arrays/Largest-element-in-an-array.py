nums = [55,32,12,-97,42,34,11]

largest = float("-inf")

n = len(nums)

for i in range(0,n):
    largest = max(largest,nums[i])

print(largest)