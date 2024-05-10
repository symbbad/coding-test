T = int(input())

def cal(k, n):
    apart = [[i for i in range(1, n+1)]]

    for f in range(1, k+1):
        temp = []
        for ho in range(n):
            temp.append(sum(apart[f-1][:ho + 1]))
        apart.append(temp)
    
    return apart[k][n-1]

result = []
for _ in range(T):
    k = int(input())
    n = int(input())
    result.append(cal(k, n))

for i in result:
    print(i)