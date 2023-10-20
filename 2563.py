N = int(input())

white_paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            white_paper[i][j] = 1

result = 0
for row in white_paper:
    result += sum(row)

print(result)