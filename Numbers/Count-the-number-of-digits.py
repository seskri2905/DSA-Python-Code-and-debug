# Using While Loop

""" n = 123

num = n

count = 0

while num > 0:
    num = num // 10
    count = count + 1 """

# Using Function 

""" n = 123


def noOfDigit(num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    
    return count

num = n
# count = 0

print(noOfDigit(num)) """

# Using log

import math

n = 9361373424

def noOfDigits(num):
    return int(math.log(num))

num = n
print(noOfDigits(num))