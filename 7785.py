import sys
input = sys.stdin.readline

N = int(input())

_set = set()
for _ in range(N):
    name, status = input().split()
    if name not in _set and status == "enter":
        _set.add(name)
    elif name in _set and status == "leave":
        _set.remove(name)

result = sorted(_set, reverse=True)

for i in result:
    print(i)