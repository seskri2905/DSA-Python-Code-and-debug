nums = [3,5,6,8,9,1,2]
n = len(nums)

def arraySortedOrNot(nums,n):
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True



result = arraySortedOrNot(nums,n)
print(result)

""" Time Complexity = O(N)
Space Complexity = O(1) """