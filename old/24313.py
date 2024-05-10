a, b, c, d, e, f = map(int, input().split())

temp = []
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c:
            temp.append((i, j))

result = [] 
for i, j in temp:
    if d*i + e*j == f:
        print(i, j)