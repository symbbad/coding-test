from collections import deque

N = int(input())

result = []

def BFS(x, y):
    que = deque()
    que.append((x, y, 0))

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    while que:
        x, y, count = que.popleft()

        if target_x == x and target_y == y:
            return count

        for i in range(8):
            moved_x = x + dx[i]
            moved_y = y + dy[i]

            if 0 <= moved_x < n and 0 <= moved_y < n and chess_map[moved_y][moved_x] == 0:
                chess_map[moved_y][moved_x] = 1
                que.append((moved_x, moved_y, count + 1))

for _ in range(N):
    n = int(input())
    chess_map = [[0]*n for _ in range(n)]

    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    result.append(BFS(x, y))

for 