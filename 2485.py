import sys
input = sys.stdin.readline

def GCM(x, y):
    while y != 0:
        x, y = y, x%y
    return x

N = int(input())
_list = [int(input()) for _ in range(N)]
_list_2 = []
count = 0

for i in range(len(_list)-1):
    _list_2.append(_list[i+1]-_list[i])

temp = GCM(_list_2[0], _list_2[1])

for i in range(len(_list_2)-2):
    temp_1 = GCM(_list_2[i+2], temp)

temp = _list[0]+temp_1

while temp <= _list[-1]:
    if temp not in _list:
        count += 1
    temp += temp_1

print(count)