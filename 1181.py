N = int(input())

array = [str(input()) for _ in range(N)]
array = list(set(array))
array.sort()
array.sort(key=len)

for i in array:
    print(i)