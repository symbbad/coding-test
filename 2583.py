import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[y][x] = True
    temp_result = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and graph[ny][nx] == 0:
            temp_result = temp_result + dfs(nx, ny)

    return temp_result

visited = [[False] * N for _ in range(M)]
result_list = []

for _ in range(K):
    x, y, x1, y2 = map(int, input().split())

    for i in range(y, y2):
        for j in range(x, x1):
            graph[i][j] = 1

for y in range(M):
    for x in range(N):
        if not visited[y][x] and graph[y][x] == 0:
            result = dfs(x, y)
            result_list.append(result)

num_result = len(result_list)

result_list.sort()

print(num_result)
print(*result_list)