# N 입력 받기
# graph 리스트로 노드 이어 받기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
result = [0] * (N+1)

for _ in range(N-1):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

def BFS(graph, result):
    que = deque()
    que.append(1)
    while que:
        i = que.popleft()
        for v in graph[i]:
            if not result[v]:
                result[v] = i
                que.append(v)
    
BFS(graph, result)

for i in range(2, N+1):
    print(result[i])