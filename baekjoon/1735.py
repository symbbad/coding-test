import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

# result_1 = _list[0]*_list[3] + _list[1]*_list[2]
# result_2 = _list[1]*_list[3]

# print(result_1, result_2)

def GCM(A, B):
    while B != 0:
        A, B = B, A%B
    return A

def LCM(A,B):
    result = (A*B) / GCM(A,B)
    return result

common = LCM(B, D)
print(LCM(B, D), GCM(B, D))
# if common == B and common == D:
#     print(A+C, common)

# elif common == B:
#     temp_1 = C * common
#     print(A+temp_1, common)

# elif common == D:
#     temp_2 = B * common
#     print(C(temp_2), common)

# else:
#     print(A*D + C*B, int(common))