N = int(input())

result = []

for i in range(2, int(N**0.5) + 1):
    while N % i == 0:
        result.append(i)
        N //= i

if N > 1:
    result.append(N)

for i in result:
    print(i)