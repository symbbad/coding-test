import math

A, B = map(int, input().split())

_list = [0]*10000001

for i in range(2, len(_list)):
    _list[i] = i

for i in range(2, int(math.sqrt(len(_list)))+1):
    if _list[i] == 0:
        continue

    for j in range(i+i, len(_list), i):
        _list[j] = 0


count = 0

for i in range(2, 10000001):
    if _list[i] != 0:
        temp = _list[i]
        while _list[i] <= B / temp:
            if _list[i] >= A / temp:
                count += 1
            temp = temp*_list[i]

print(count)