import sys
from collections import deque

count = 0

def dfs(row, col):
    global count
    if vaild(row, col):
        return
    if matrix[row][col] == 1:
        count += 1
        matrix[row][col] = 0
        dfs(row+1,col)
        dfs(row,col+1)
        dfs(row-1,col)
        dfs(row,col-1)

def vaild(row, col):
    if row<0 or col<0 or col>=n or row>=n:
        return True
    return False

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))
complex_num = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            dfs(row, col)
            complex_num.append(count)
            count = 0

complex_num.sort()

print(len(complex_num))
for i in complex_num:
    print(i)