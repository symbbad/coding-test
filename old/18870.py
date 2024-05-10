N = int(input())
array = list(map(int, input().split()))

r1 = sorted(list(set(array)))
d1 = {r1[i]: i for i in range(len(r1))}

for i in array:
    print(d1[i], end=' ')