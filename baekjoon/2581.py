N = int(input())
M = int(input())

_list = [0]*(M+1)

_result = 0

for i in range(2, M+1):
    _list[i] = i
    
for i in range(2, int(M**0.5)+1):
    if _list[i] == 0:
        continue
    
    for j in range(i+i, M+1, i):
        _list[j] = 0

for i in range(N, M+1):
    if _list[i] == 0:
        continue
    else:
        _result = _list[i]
        break

if _result == 0:
    print(-1)
else:
    print(sum(_list[N: M+1]))
    print(_result)