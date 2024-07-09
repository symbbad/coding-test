# TESTCASE 입력 받기 : case_num

# dy = [1, -1, 0, 0]
# dx = [0, 0, 1, -1]

# for num:
#     가로, 세로, 양배추 수 입력 받기 : col, row, num
#     양배추 밭 입력 선언 혹은 초기화 : map : 인라인코드
#     결과 : result

#     for num:
#         x, y 좌표 입력 받기
#         map[y][x] = 1

#     for row:
#         for col:
#             if dfs(row, col):
#                 result += 1

# def dfs <- row, col (DFS, BFS 함수의 역할은 인접해 있는 배추를 탐색하며 0 으로 바꿔줌. 다 바꾸면 끝나아함)
#     if vaild:
#         return
#     if map[y][x] == 1:
#         map[y][x] = 0

# def bfs <- row, col
#     que 선언 : que
#     que.append((row, col))
#     while que
#         ...
#         if 유효성 검사
            
#         if 좌표가 1인 경우
#             좌표 0 초기화


from collections import deque

movex = [0, 0, 1, -1]
movey = [1, -1, 0, 0]

num = int(input())

def BFS(x, y):
    que = deque()
    que.append((x, y))
    matrix[y][x] = 0

    while que:
        dx, dy = que.popleft()
        for i in range(4):
            new_x = dx + movex[i]
            new_y = dy + movey[i]

            if new_x < 0 or new_x >= col or new_y < 0 or new_y >= row:
                continue

            if matrix[new_y][new_x] == 1:
                matrix[new_y][new_x] = 0
                que.append((new_x, new_y))
    return


for _ in range(num):
    col, row, beachu = map(int, input().split())
    matrix = [[0]*col for _ in range(row)]
    result = 0

    for _ in range(beachu):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    for i in range(row):
        for j in range(col):
            BFS(j, i)
            result += 1

    print(result)