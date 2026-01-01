n = -1

num = abs(n)

def fact(num):
    if (num == 1 or num == 0):
        return 1
    return num * fact(num - 1)

result = fact(num)

print(f'The factorial of {num} is {result}')