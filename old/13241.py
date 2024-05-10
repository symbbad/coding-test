import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def LCM(A, B):
    result = (A*B) / GCM(A, B)
    
    return result

def GCM(A, B):
    while B != 0:
        A, B = B, A%B
    return A

print(int(LCM(A, B)))