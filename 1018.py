N, M = map(int, input().split())

board = []

min_repair = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        index_W = 0
        index_B = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != "W":
                        index_W = index_W+1
                    if board[a][b] != "B":
                        index_B = index_B+1

                else:
                    if board[a][b] != "W":
                        index_B = index_B+1
                    if board[a][b] != "B":
                        index_W = index_W+1
        min_repair.append(index_B)
        min_repair.append(index_W)

print(min(min_repair))