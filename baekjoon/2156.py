import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 10000
wines = [int(input()) for _ in range(n)]

dp[0] = wines[0]
dp[1] = wines[0]+wines[1]
dp[2] = max(wines[2]+wines[1], wines[0]+wines[2], dp[1])

for i in range(3, n):
    dp[i] = max(wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3], dp[i-1])

print(max(dp))
    