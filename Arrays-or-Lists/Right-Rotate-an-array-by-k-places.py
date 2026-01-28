# Brute

""" nums = [7,2,3,9,5,6]

k = 3

for _ in range(0,k):
    e = nums.pop()
    nums.insert(0,e)

print(nums) """

# Non repetitive of rotation, when size of array > rotation, then rotation % length of array => Which is also a brute

nums = [7,2,3,9,5,6]

n = len(nums)

k = 3

rotations = k % n

for _ in range(0,rotations):
    e = nums.pop()
    nums.insert(0,e)   # insert() time complexity is O(N)

print(nums)

""" Time Complexity = O(rotations * N)
    Space Complexity = O(1)"""

