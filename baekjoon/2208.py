N, M = map(int, input().split())

dp = [int(input()) for _ in range(N)]
_max = 0
_count = 0
_index = 0

while _count < M:
    if dp[_index] == -1:
        _index += 1
        pass

    else:
        _max = max(dp[_index] + dp[_index-1], dp[_index])
print(max(dp))