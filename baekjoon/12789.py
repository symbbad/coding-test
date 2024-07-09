import sys
input = sys.stdin.readline

_ = int(input())

stand = list(map(int, input().split()))
stack = []
target = 1

while stand:
    if stand[0] == target:
        stand.pop(0)
        target += 1
    else:
        stack.append(stand.pop(0))

    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break


if stack:
    print("Sad")
else:
    print("Nice")