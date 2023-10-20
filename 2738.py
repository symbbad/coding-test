N, M = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(N)]
matrix_2 = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(M):
        print(matrix_1[row][col]+matrix_2[row][col], end=' ')
    print()