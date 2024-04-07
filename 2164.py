import sys
from collections import deque
input = sys.stdin.readline().rstrip

def logic(n):
    if n == 1:
        return 1

    queue = deque(range(1, n+1))

    while len(queue) > 1:
        queue.popleft()
        queue.rotate(-1)

    return queue[0]


N = int(input())
print(logic(N))