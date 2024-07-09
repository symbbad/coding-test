import sys
sys.setrecursionlimit(10000) 
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 0

for _ in range(M):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


def dfs(graph, visited, node):
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(graph, visited, next_node)

for i in range(1, len(graph)):
    if not visited[i]:
        dfs(graph, visited, i)
        count += 1

print(count)