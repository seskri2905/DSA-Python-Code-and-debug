# Naive Approach

n = 5
num = n

a = 0
b = 1
next = b
count = 1

while count <= num:
    print(next,end=' ')
    count+=1
    a,b = b,next
    next = a + b
    