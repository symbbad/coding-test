matrix = [list(map(int, input().split())) for _ in range(9)]

max_value = 0

for i in range(9):
    temp = max(matrix[i])
    if max_value < temp:
        max_value = temp

print(max_value)      

for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_value:
            print(i+1, j+1)