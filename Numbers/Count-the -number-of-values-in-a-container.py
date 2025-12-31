# Brute Force

# Constraints
# 1) 1 <= n[i] <= 10
# 2) n can have 10^8 elements
# 3) m can have 10^8 elements

""" n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for num in m:
    count = 0
    for x in n:
        if(num == x):
            count += 1
            
    print(f'{num} comes {count} times')
 """
# Time Complexity = O(M * N)
# Space Complexity = O(1)

# So, the worst case scenario will be O(10^8 * 10^8) =>  O(10^16) > O(10^8). So, that leads to TLE

# Optimal