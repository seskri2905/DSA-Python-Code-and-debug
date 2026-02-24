def linearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return "Element not found"



nums = [1,2,3,4,5,6,77,8,9]
target = 22

result = linearSearch(nums,target)
print(result)