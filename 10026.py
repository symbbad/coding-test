import sys
sys.setrecursionlimit(10000)

N = int(input())

matrix = []

for _ in range(N):
    temp = input()
    matrix.append([ord(char) for char in temp])

def DFS(col, row, visited, def_matrix):
    visited[row][col] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        drow = row + dy[i]
        dcol = col + dx[i]

        if 0 <= dcol < N and 0 <= drow < N and def_matrix[drow][dcol] == def_matrix[row][col] and not visited[drow][dcol]:
            DFS(dcol, drow, visited, def_matrix)

RGB_result = 0
B_result = 0

visited = [[False]*N for _ in range(N)]


for col in range(N):
    for row in range(N):
        if not visited[row][col]:
            DFS(col, row, visited, matrix) 
            RGB_result += 1

visited = [[False]*N for _ in range(N)]


for col in range(N):
    for row in range(N):
        if matrix[row][col] == 82 or matrix[row][col] == 71: 
            matrix[row][col] = 153

for col in range(N):
    for row in range(N):
        if not visited[row][col]:
                DFS(col, row, visited, matrix)
                B_result += 1

print(RGB_result, B_result)