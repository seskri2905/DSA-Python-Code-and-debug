num = [1,2,3,4,5,6]
left = 1
right = 3

def reverseArray(num,left,right):
    if left >= right:
        return
    
    num[left], num[right] = num[right], num[left]   # Tuple unpacking - Instead of using temp value tuple unpacking is used. Tuple unpacking is a Python feature that allows you to assign values from a tuple (or any iterable) to multiple variables in a single, concise statement. This is often used for swapping values or working with multiple items at once.
    reverseArray(num,left + 1,right - 1)


reverseArray(num,left,right)

# for i in range(len(num)):
#     print(num[i],end=' ')

print(*num)