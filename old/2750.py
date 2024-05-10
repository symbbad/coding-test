import sys

array = []

N = int(input())
for _ in range(N):
    array.append(int(input()))
array.sort()

print(*array)