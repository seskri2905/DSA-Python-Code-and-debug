# Brute force

""" import math

n = 1534
num = n
number_of_digit = n
is_armstrong = 0
count = 0

while number_of_digit > 0:
    number_of_digit = number_of_digit // 10
    count = count + 1

while num > 0:
    mod = num % 10
    is_armstrong = is_armstrong + math.pow(mod,count)
    num = num // 10

if n == is_armstrong:
    print('It is a armstrong number')
else:
    print('It is not a armstrong number') """

# Counting number of digit using length function
import math

n = 1534
num = n

number_of_digit = len(str(num))

is_armstrong = 0

while num > 0:
    mod = num % 10
    is_armstrong = is_armstrong + math.pow(mod,number_of_digit)
    num = num // 10

if n == is_armstrong:
    print('It is a armstrong number')
else:
    print('It is not an armstrong number')
