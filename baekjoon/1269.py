import sys
input = sys.stdin.readline

N, M = map(int, input().split())

_dict_1 = set(map(int, input().split()))
_dict_2 = set(map(int, input().split()))

print(len(_dict_1-_dict_2)+len(_dict_2-_dict_1))