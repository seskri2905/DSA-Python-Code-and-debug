# Brute

""" def zeroesToEnd(arr):
    n = len(arr)

    zero_temp = []
    non_zero_temp = []
    
    for i in range(n):
        if arr[i] == 0:
            zero_temp.append(arr[i])
        else:
            non_zero_temp.append(arr[i])
    
    arr[:] = non_zero_temp[:] + zero_temp[:]

arr = [1,0,2,4,3,0,0,3,5,1]

zeroesToEnd(arr)

for val in range(len(arr)):
    print(arr[val],end=' ') """

""" Time Complexity = O(N)
Space Complexity = O(N) """

# Optimal

def zeroesToEnd(arr):
    n = len(arr)

    if n == 1:
        return

    j = 0


    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1


arr = [1,0,2,4,3,0,0,3,5,1]

zeroesToEnd(arr)

for val in range(len(arr)):
    print(arr[val],end=' ')