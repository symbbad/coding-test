import math

M, N = map(int, input().split())

_list = [0]*(N+1)

for i in range(2, N+1):
    _list[i] = i

for i in range(2, int(math.sqrt(N))+1):
    if _list[i] == 0:
        continue

    for j in range(i+i, N+1, i):
        _list[j] = 0
            
for i in range(M, N+1):
    if _list[i] != 0:
        print(i)