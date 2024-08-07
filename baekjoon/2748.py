import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 1, 1, 2]

for i in range(4, N+1):
    dp.append(dp[i-1]+dp[i-2])
    
print(dp[N])