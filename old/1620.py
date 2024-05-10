N, M = map(int, input().split())

_dict_1 = {}
_dict_2 = {}

for i in range(N):
    temp = input().rstrip()
    _dict_1[i+1] = temp
    _dict_2[temp] = i+1
    
for i in range(M):
    temp = input().rstrip()
    if temp.isdigit():
        print(_dict_1[int(temp)])
    else:
        print(_dict_2[temp])