import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))


for i in m_list:
    chk = False

    start = 0
    end = len(n_list) - 1

    while start <= end:
        midi = int((start + end) / 2)
        midv = n_list[midi]

        if midv > i:
            end = midi-1
        elif midv < i:
            start = midi+1
        else:
            chk = True
            break

    if chk:
        print(1)
    else:
        print(0)
