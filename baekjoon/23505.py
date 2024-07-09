import sys

N, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort()

print(array[len(array)-k])