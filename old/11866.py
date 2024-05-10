import sys
from collections import deque

input = sys.stdin.readline().rstrip


N, K = map(int, input().split())
queue = deque(range(1, N+1))
_list = []

for _ in range(N):
    queue.rotate(-(K-1))
    temp = queue.popleft()
    _list.append(temp)

str = "<"
for i in range(len(_list)-1):
    str = str + f"{_list[i]}, "

str = str + f"{_list[-1]}>"

print(str)