""" value = "madam"

left = 0
right = len(value) - 1

def palindrome(value,left,right):
    while left < right:
        if value[left] != value[right]:
            return False
        
        return True
    palindrome(value,left+1,right-1)

result = palindrome(value,left,right)

print(f'The {value} is {result}')
     """

value = "chennai"

def palindrome(value, left, right):
    if left >= right:
        return True

    if value[left] != value[right]:
        return False

    return palindrome(value, left + 1, right - 1)

result = palindrome(value, 0, len(value) - 1)

if result:
    print(f"The {value} is a palindrome")
else:
    print(f"The {value} is not a palindrome")