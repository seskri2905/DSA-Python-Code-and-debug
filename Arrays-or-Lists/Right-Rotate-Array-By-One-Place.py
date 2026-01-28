""" nums = [5,-2,3,9,0,6,10,7]

n = len(nums)

nums[:] = [nums[n-1]] + nums[0:n-1]

print(nums) """

""" Time Complexity = O(1) + O(N - 1) => O(N)
    Space Complexity = O(N) Key point ⚠️

Even though:

You modify the same list object (nums[:])

And don't create a new variable

👉 Python still creates temporary lists in memory, so extra space is used.""" 

nums = [5,-2,3,9,0,6,10,7]

n = len(nums)

temp = nums[n-1]

for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)

""" Time Complexity = O(N - 1) Which is similar to O(1)
    Space Complexity = O(1) """