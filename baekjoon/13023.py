import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
arrive = False

def DFS(n, depth):
    global arrive

    if depth == 5:
        arrive = True
        return
    else:
        visited[n] = True
        for i in graph[n]:
            if not visited[i]:
                DFS(i, depth+1)
        visited[n] = False

for _ in range(M):
    v, e = map(int,input().split())
    graph[v].append(e)
    graph[e].append(v)

for i in range(N):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)