# GeeksForGeeks

# Brute Force = Using temp array 
""" def reverseArray(arr):
    n = len(arr)
    temp = [0] * n

    for i in range(n):
        temp[i] = arr[n-i-1]
    
    for i in range(n):
        arr[i] = temp[i]


arr = [1,2,3,4,5,6]
reverseArray(arr)

for val in arr:
    print(val,end=' ') """

""" Time Complexity:O(N)
    Space Complexity:O(N) """

# Brute => Two Pointer

def reverseArray(arr):
    
    n = len(arr)

    left = 0
    right = n - 1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1

arr = [1,2,3,4,5,6]
reverseArray(arr)

for i in range(len(arr)):
    print(arr[i],end=' ')


