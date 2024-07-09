import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
N = int(input())

for _ in range(N):
    num =  list(map(int, input().strip().split()))
    _len = len(queue)
    if num[0] == 1:
        queue.appendleft(num[1])
    elif num[0] == 2:
        queue.append(num[1])
    elif num[0] == 3:
        print(queue.popleft() if _len else -1)
    elif num[0] == 4:
        print(queue.pop() if _len else -1)
    elif num[0] == 5:
        print(len(queue))
    elif num[0] == 6:
        print(0 if _len else 1)
    elif num[0] == 7:
        print(queue[0] if _len else -1)
    elif num[0] == 8:
        print(queue[-1] if _len else -1)