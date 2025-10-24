import sys

N, K = map(int,sys.stdin.readline().split())

dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(1,K+1):
    tmp = 1
    for j in range(1,N+1):
        tmp = (tmp +dp[i-1][j])%1e9
        dp[i][j] = tmp 

print(int(dp[K][N]%1e9))

