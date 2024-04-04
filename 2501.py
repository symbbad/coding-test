N, K = map(int, input().split())

_list = []

for i in range(1, N+1):
    if N % i == 0:
        _list.append(i)

if len(_list) < K:
    print(0)
else:
    print(_list[-K+1])