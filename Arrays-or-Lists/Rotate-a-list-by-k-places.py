# GeeksForGeeks

# Brute - last element of a list as temp and adding in the front

""" def rotateClockwise(arr,k):
    if k==0:
        return
    
    n  = len(arr)

    temp = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp

    rotateClockwise(arr,k-1)


arr = [1,2,3,4,5,6]
k = 2
rotateClockwise(arr,k)
for val in arr:
    print(val,end=' ') """

""" Time Complexity = O(n * k)
    Space Complexity = O(k)
     """

# Better - Slicing - Source: CodeandDebug.in

""" def rotateClockwise(arr,k):
    n = len(arr)

    k = k % n

    arr[:] = arr[n-k:] + arr[:n-k]  # k + (n-k)



arr = [1,2,3,4,5,6]
k = 2
rotateClockwise(arr,k)
for val in arr:
    print(val,end=' ') """

""" Time Complexity : O(n) => constant time + k + (n-k) + arr[:] assignment
    Space Complexity : O(n) """

# Optimal - Using Reversal Algorithm - GeeksForGeeks

def rotateClockwise(arr,k):
    n = len(arr)
    if n == 0:
        return
    
    k = k % n

    arr[n-k:]=reversed(arr[n-k:])

    arr[:n-k]=reversed(arr[:n-k])

    arr[:] = reversed(arr)


arr = [1,2,3,4,5,6]
k = 2
rotateClockwise(arr,k)

for val in arr:
    print(val,end=' ')

""" Time Complexity = O(n) 
    Space Complexity = O(n) """
