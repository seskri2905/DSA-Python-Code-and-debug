n = 121

num = n
is_palindrome = 0

while num > 0:
    mod = num % 10
    is_palindrome = is_palindrome * 10 + mod
    num = num // 10

if n == is_palindrome:
    print('Number is Palindrome')
else:
    print('Number is not palindrome')