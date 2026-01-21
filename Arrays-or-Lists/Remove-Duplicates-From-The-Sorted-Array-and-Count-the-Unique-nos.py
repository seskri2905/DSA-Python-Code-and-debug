# Brute Force - Dictionary

""" nums = [1,1,1,2,3,4,4,7,9,9,9,10]

n = len(nums)
freq_map = {}

for i in range(0,n):
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:
    nums[j] = k
    j = j + 1

print(j) """

""" Time Complexity = O(2N) Which is smilar to O(N)
    Space Complexity = O(N) Beacause it depends on no. """

# Optimal - Two Pointers Approach

nums = [1,1,1,2,3,4,4,7,9,9,9,10]

n = len(nums)

if n == 1:
    print(n)

i = 0
j = i + 1

while j < n:
    if nums[j] != nums[i]:
        i = i + 1
        nums[i],nums[j] = nums[j],nums[i]
    
    j+=1

print(i + 1)