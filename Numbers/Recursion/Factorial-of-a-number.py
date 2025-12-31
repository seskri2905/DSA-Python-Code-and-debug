n = 5

num = n

def fact(num):
    if (num == 1):
        return 1
    return num * fact(num - 1)

result = fact(num)

print(f'The factorial of {num} is {result}')