n = 2

num = n

def fact(num):
    if (num == 1):
        return 1
    return num * fact(num - 1)

print(f'The factorial of {num} is {fact(num)}')