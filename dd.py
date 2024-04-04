import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

M, N, K = map(int, input().split())
matrix = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def DFS(x, y):
    visited[y][x] = True
    area = 1

    for dx, dy in dn:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] and matrix[ny][nx] == 0:
            area += DFS(nx, ny)

    return area

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[j][i] = 1

area = []
for i in range(M):
    for j in range(N):
        if not visited[i][j] and matrix[i][j] == 0:
            area.append(DFS(j, i))

area.sort()
print(len(area))
print(*area)