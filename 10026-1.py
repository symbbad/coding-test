from collections import deque

N = int(input())

matrix = []

for _ in range(N):
    temp = input()
    matrix.append([ord(char) for char in temp])

def BFS(col, row, visited, def_matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    que = deque()
    que.append((col, row))

    while que:
        c, r = que.popleft()

        for i in range(4):
            drow = r + dy[i]
            dcol = c + dx[i]
        
            if 0 <= dcol < N and 0 <= drow < N and def_matrix[drow][dcol] == def_matrix[r][c] and not visited[drow][dcol]:
                visited[drow][dcol] = True
                que.append((dcol, drow))

RGB_result = 0
B_result = 0

visited = [[False]*N for _ in range(N)]

for col in range(N):
    for row in range(N):
        if not visited[row][col]:
            visited[row][col] = True
            BFS(col, row, visited, matrix) 
            RGB_result += 1

visited = [[False]*N for _ in range(N)]

for col in range(N):
    for row in range(N):
        if matrix[row][col] == 82 or matrix[row][col] == 71: 
            matrix[row][col] = 153

for col in range(N):
    for row in range(N):
        if not visited[row][col]:
            visited[row][col] = True
            BFS(col, row, visited, matrix)
            B_result += 1

print(RGB_result, B_result)