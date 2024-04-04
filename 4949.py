import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()

    if string == ".":
        break

    stack = []
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)

        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        print("no")
    else:
        print("yes")