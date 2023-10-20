dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

num = int(input())

def DFS(x, y):
    if x < 0 or x >= col or y < 0 or y >= row:
        return False
    if matrix[y][x] == 1:
        matrix[y][x] = 0
        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        return True
    return False

for _ in range(num):
    col, row, beachu = map(int, input().split())
    matrix = [[0]*col for _ in range(row)]
    result = 0

    for _ in range(beachu):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    for i in range(row):
        for j in range(col):
            if DFS(j, i):
                result += 1

    print(result)