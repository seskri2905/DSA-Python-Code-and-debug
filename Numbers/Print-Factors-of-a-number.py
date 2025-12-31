# Brute Force

""" n = 20
num = n
result = []

for i in range(1,num + 1):
    if num % i == 0:
        result.append(i)

print(result) 

Time Complexity = O(N)
Space Complesity = O(k), where k is the amount of factors stored in the result

"""


# Divide by n // 2

""" n = 20
num = n
result = []

for i in range(1,num//2):
    if num % i == 0:
        result.append(i)

result.append(num)

print(result) 

Time Complexity = O(N/2) => O(N * 1/2) => O(N), So, O(N) is closely equal to O(N/2)
Space Complexity = O(k), where k is the amount of factors stored in the result

"""

# Optimal Solution

import math

n = 36
num = n

result = []

for i in range(1,int(math.sqrt(num)) + 1):
    if(num % i == 0):
        result.append(i)
    if(num // i != i):
        result.append(num // i)

result.sort()

print(result)

# Time Complexity = O(sqrt(N)) + O(N log N) i.e., For loop goes upto sqrt(n) so, O(sqrt(N)). And sorting is always O(N log N)
# Space Complexity = O(k) 