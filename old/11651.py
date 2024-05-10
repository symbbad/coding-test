import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    [a, b] = map(int, input().split())
    array.append([a, b])

array.sort(key= lambda x: (x[1], x[0]))

for i in range(n):
    print(array[i][0], array[i][1])