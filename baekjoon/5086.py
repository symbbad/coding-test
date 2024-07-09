_list = []

while True:    
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    _list.append([N, M])

for i in _list:
    N = i[0]
    M = i[1]
    
    if N >= M:
        if N % M == 0:
            print("multiple")
        else:
            print("neither")

    elif N < M:
        if M % N == 0:
            print("factor")
        else:
            print("neither")