n = 6789

num = n
rev = 0

while num > 0:
    mod = num % 10
    rev = rev * 10 + mod
    num = num // 10

print(rev)
