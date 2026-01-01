n = 16
num = n

def fibonacciOfANumber(num):
    if num == 0 or num == 1:
        return num
    return fibonacciOfANumber(num - 1) + fibonacciOfANumber(num - 2)

result = fibonacciOfANumber(num)

print(f'The Fibobacci of {num} is {result}')