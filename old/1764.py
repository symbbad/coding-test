import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# _dict = set([str(input().rstrip()) for _ in range(N)])
# result = []
# for _ in range(M):
#     word = str(input().rstrip())
#     if word in _dict:
#         result.append(word)

# result.sort()
# print(len(result))
# for i in result:
#     print(str(i))

_dict_1 = set([str(input().rstrip()) for _ in range(N)])
_dict_2 = set([str(input().rstrip()) for _ in range(M)])

result = sorted(list(_dict_1&_dict_2))
print(len(result))
for i in result:
    print(i)