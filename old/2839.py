# N = int(input())
# count = 0

# while N > 0:
#     if N % 5 == 0:
#         count += N // 5
#         N = 0
#     else:
#         N -= 3 
#         count += 1

# if N == 0:
#     print(count)
# else:
#     print(-1)



def sugar_delivery(N):
    dp = [-1] * (N + 1)  # dp 배열 초기화

    # 초기 상태 설정
    dp[0] = 0  # 0킬로그램 설탕은 봉지를 사용하지 않음
    sizes = [3, 5]  # 가능한 봉지 크기

    for size in sizes:
        for i in range(size, N + 1):
            if dp[i - size] != -1:
                if dp[i] == -1 or dp[i] > dp[i - size] + 1:
                    dp[i] = dp[i - size] + 1

    return dp[N]

N = int(input())  # 배달해야 할 설탕의 무게
result = sugar_delivery(N)
print(result)
print()