N = int(input())

_list = list(map(int, input().split()))

_list_1 = [0]*(1001)
result = 0

for i in range(2, 1001):
    _list_1[i] = i

for i in range(2, int(1001**0.5)+1):
    if _list_1[i] == 0:
        continue
    
    for j in range(i+i, 1001, i):
        _list_1[j] = 0
        

for i in _list:
    if _list_1[i] != 0:
        result += 1
    
print(result)