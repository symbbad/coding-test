# N, M = map(int, input().split())

# _set = set()

# for _ in range(N+M):
#     _set.add(input())

# print((N+M)-len(_set))


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
count = 0 
_set = set([input().rstrip() for i in range(N)])

_list = list(input().rstrip() for i in range(M))

for i in _list:
    if i in _set:
        count += 1

print(count)
