# import sys
# input = sys.stdin.readline

# N = int(input())
# l1 = list(map(int, input().split()))

# M = int(input())
# l2 = list(map(int, input().split()))

# result = [1 if i in l1 else 0 for i in l2]
# print(*result)

# n = int(input())  # 상근이가 가지고 있는 숫자 카드의 개수
# cards = list(map(int, input().split())) # 상근이가 가지고 있는 숫자 카드
# m = int(input())  # 확인해야 할 수의 개수
# numbers_to_check = list(map(int, input().split()))  # 확인해야 할 수들

# result = [1 if num in cards else 0 for num in numbers_to_check]
# print(' '.join(map(str, result)))

def bisearch(target, data, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if data[mid] == target:
        return 1
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
        
    return bisearch(target, data, start, end)

N = int(input())
l1 = list(map(int, input().split()))

M = int(input())
l2 = list(map(int, input().split()))

l1.sort()
for i in l2:
    print(bisearch(i,l1, 0, len(l1)-1, ), end=' ')