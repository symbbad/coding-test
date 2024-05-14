import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    n, e = map(int, input().split())
    graph[n].append(e)
    graph[e].append(n)

for i in range(N+1):
    graph[i].sort()

def DFS(n):
    print(n, end=" ")
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            DFS(i)

def BFS(n):
    queue = deque()
    queue.append(n)
    visited[n] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)



DFS(V)

print()
visited = [False] * (N+1)

BFS(V)