import sys
input = sys.stdin.readline
 
from collections import deque
 
N = int(input())
queue = deque()

for _ in range(N):
    order = input().split()    
    
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        print(-1) if len(queue) == 0 else print(queue.popleft())
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(1) if len(queue) == 0 else print(0)
    elif order[0] == 'front':
        print(-1) if len(queue) == 0 else print(queue[0])
    elif order[0] == 'back':
        print(-1) if len(queue) == 0 else print(queue[-1])