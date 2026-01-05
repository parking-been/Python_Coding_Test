import sys

N, M = map(int ,sys.stdin.readline().split())

dp = [[1e9]*(N+1) for _ in range(N+1)]

small = set()
for i in range(M):
    small.add(int(sys.stdin.readline().strip()))

dp[1][0] = 0

for i in range(2, N+1):
    if i in small:
        continue
    for j in range(1, N):
        dp[i][j] = min(dp[i-j][j-1],dp[i-j][j],dp[i-j][j+1])+1

if min(dp[N]) == 1e9:
    print(-1)
else:
    print(min(dp[N]))
