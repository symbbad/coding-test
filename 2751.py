import sys

N = int(sys.stdin.readline())

array = []

for _ in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()

for i in range(N):
    print(array[i])