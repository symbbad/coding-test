import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
vistied = [False] * (n+1)

def DFS(v):
    vistied[v] = True
    for i in graph[v]:
        if not vistied[i]:
            DFS(i)

for _ in range(m):
    node, edge = map(int, input().split())
    graph[node].append(edge)
    graph[edge].append(node)

count = 0

for i in range(1, n+1):
    if not vistied[i]:
        count += 1
        DFS(i)

print(count)