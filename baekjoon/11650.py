import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    [a, b] = map(int, input().split())
    array.append([a, b])

r_array = sorted(array)

for i in range(n):
    print(r_array[i][0], r_array[i][1])