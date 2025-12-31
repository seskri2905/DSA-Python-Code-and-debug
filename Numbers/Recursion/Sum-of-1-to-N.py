n = 10

num = n
i = 1

def sumOfOneToN(i):
    if i > num:
        return 0
    return i + sumOfOneToN(i + 1)




print(sumOfOneToN(i))