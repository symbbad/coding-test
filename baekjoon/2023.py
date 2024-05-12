import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10):
            if isPrime(num*10 + i):
                DFS(num*10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)