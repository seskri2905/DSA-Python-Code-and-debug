# Ascending Order

""" nums = [5,7,8,4,1,6,9,2]

def selectionSort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i + 1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]

selectionSort(nums)

print(nums) """
        

#  Descending Order

""" nums = [5,7,8,4,1,6,9,2]

def selectionSort(nums):
    n = len(nums)
    for i in range(0,n):
        max_index = i
        for j in range(i + 1,n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i],nums[max_index] = nums[max_index],nums[i]

selectionSort(nums)

print(nums)
 """

""" TC = O(N(N+1/)/2)
SC = O(1) """