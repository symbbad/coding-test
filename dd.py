n = int(input())

for i in range(1, n):
    blank = " " * (n - i)
    star = "*" * (2*i - 1)

    print(blank + star)

print("*"*(2*n-1))

for i in range(n-1, 0, -1):
    blank = " " * (n - i)
    star = "*" * (2*i - 1)

    print(blank + star)