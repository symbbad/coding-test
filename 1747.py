N = int(input())

temp = True

if N == 1:
    temp = False
    print(1)
    
while temp:
    chk = True
    for i in range(2, int(N**0.5)):
        if N % i == 0:
            chk = False
            break
    
    if chk:
        temp = str(N)
        if temp == temp[::-1]:
            print(N)
            break
    
    N += 1