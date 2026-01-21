# Best
""" nums = [55,32,97,-55,11,87,2]

largest = float("-inf")
second_largest = float("-inf")

n = len(nums)

for i in range(0,n):
    largest = max(largest,nums[i])

for i in range(0,n):
    if nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest) """

""" Time Complexity O(2N) which is similar to O(N)  2N because of using 2 for loops
    Space complexity = O(1) """

# Optimal

nums = [55,32,97,-55,11,87,2]

largest = float("-inf")
second_largest = float("-inf")

n = len(nums)

for i in range(0,n):
    if nums[i] > largest:
        """ second_largest = largest
        largest = nums[i] """
        second_largest,largest = largest,nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
print(second_largest)

""" Time Complexity = O(N)
    Space Compplexity = O(1) """
