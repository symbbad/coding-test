T = int(input())

result = [[0,0,0,0] for _ in range(T)]
cal = [25, 10, 5, 1]

for i in range(T):
    change = int(input())
    for idx in range(4):
        result[i][idx] = (change//cal[idx])
        change = change%cal[idx]

for i in range(T):
    for j in range(4):
        print(result[i][j], end= ' ')
    print()