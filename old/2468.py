import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
heights = set()
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, height):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > height:
            dfs(nx, ny, height)

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    heights.update(row)

result = 0

for h in heights:
    visited = [[False] * N for _ in range(N)]
    temp_result = 0

    for col in range(N):
        for row in range(N):
            if graph[col][row] > h and not visited[col][row]:
                temp_result += 1
                dfs(col, row, h)

    result = max(result, temp_result)

print(result)