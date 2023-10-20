from collections import deque

size = int(input())
map = [list(map(int, input())) for _ in range(size)]

result = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt_std = 0

def vaild_test(y, x):
    return 0 <= x < size and 0 <= y < size

def dfs(y, x):
    global cnt_std
    if vaild_test(y, x) and map[y][x] == 1:
        map[y][x] = 0
        cnt_std += 1
        for i in range(4):
            dfs(y+dy[i], x+dx[i])

def bfs(y, x):
    que = deque()
    que.append((0, 0))
    while que:
        y, x = que.popleft()
        if vaild_test(y, x) and map[y][x] == 1:

for row in range(size):
    for col in range(size):
        if map[row][col] == 1:
            dfs(row, col)
            bfs(row, col)
            result.append(cnt_std)
            cnt_std = 0 

result.sort()

print(len(result))
for i in result:
    print(i)