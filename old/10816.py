import sys
input = sys.stdin.readline

_ = int(input())
l1 = list(map(int, input().split()))

_ = int(input())
l2 = list(map(int, input().split()))

_dict = {}

for i in l1:
    if i in _dict:
        _dict[i] += 1
    else:
        _dict[i] = 1
        
print(' '.join(str(_dict[i]) if i in _dict else '0' for i in l2))