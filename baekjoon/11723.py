import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    word = input().strip()

    if word == "all":
        print(word)
        S = set(range(1, 21))
    elif word == "empty":
        S = set()
    else:
        word, x = word.split()
        x = int(x)

        if word == "add":
            S.add(x)
        elif word == "remove":
            S.discard(x)
        elif word == "check":
            print(1 if x in S else 0)
        elif word == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)
