# Brute

""" def missingNumberInAnArray(nums,n):  
    for i in range(0,n+1): # This is iterating n times
        if i not in nums: # This is iterating n times
            return i


nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

answer = missingNumberInAnArray(nums,n)
print(answer) """

""" Time Complexity = O(N^2)
Space Complexity = O(1) """

# Better 

""" def missingNumberInAnArray(nums,n):
    n,freq = len(nums),{}

    for i in range(0,n+1): #O(N)
        freq[i] = 0

    for num in nums:  #O(N)
        freq[num] = 1

    for key,value in freq.items():  #O(N)
        if value == 0:
            return key



nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

answer = missingNumberInAnArray(nums,n)
print(answer)
 """
""" Time Complexity = O(3N) => O(N)
Space Complexity = O(N)  """

#Optimal

nums=[9,6,4,2,3,5,7,0,1]
n=len (nums)
n_sum=(n*(n+1))//2
sum=0
for i in nums:
  sum=sum+i
missing_number=n_sum-sum
print(missing_number)

""" Time Comolexity = O(N)
Space Complexity = O(1) """