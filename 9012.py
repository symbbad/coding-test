import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    string = str(input())
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) >= 1 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
    if len(stack) >= 1:
        print("NO")
    else:
        print("YES")