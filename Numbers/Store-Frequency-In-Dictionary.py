# Method 1:Traditional way without using get()[using if-else instead of get()]

""" nums = [5,6,77,7,7,1,2]

freq_map = dict()

for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)

# Time Complexity: O(N)
# Space Complexity: O(N), Because what if all nos. are unique """

# Method 2: By using get()

nums = [5,6,77,7,7,1,2]

x = 7

hash_map = dict()

n = len(nums)

for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1     # get(nums[i],0) means, it gets nums[i] if it exists in the dict. Else 0.

# print(hash_map)
print(f'Frequency of {x} is {hash_map[x]}')