import sys

while True:
    N = int(sys.stdin.readline().strip())
    if N == -1:
        break
    
    _list = []
    for i in range(1, N//2 + 1):
        if N % i == 0:
            _list.append(i)
            
    if sum(_list) == N:
        print(f"{N} =", " + ".join(map(str, _list)))
    else:
        print(f"{N} is NOT perfect.")