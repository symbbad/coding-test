from collections import deque

row, col = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(row)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, 1, -1]

def valid(col, row, moved_x, moved_y, visited):
    if 0 <= moved_x < col and 0 <= moved_y < row:
        if miro[moved_y][moved_x] == 1 and not visited[moved_y][moved_x]:
            return True

def BFS(col, row):
    que = deque([(0, 0)])
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            moved_x = x + move_x[i]
            moved_y = y + move_y[i]

            if valid(col, row, moved_x, moved_y, visited):
                visited[moved_y][moved_x] = True
                que.append((moved_x, moved_y))

                if moved_x == col - 1 and moved_y == row - 1:
                    return visited[y][x] + 1  # 최단 경로의 길이 반환

    return -1  # 도착점에 도달하지 못한 경우

result = BFS(col, row)

if result != -1:
    print(result)
else:
    print("도착점에 도달할 수 없습니다.")