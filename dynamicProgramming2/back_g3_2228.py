import sys
import math

N, M = map(int, sys.stdin.readline().split())

arr = [0]
sum = [0]
tmp = 0
for i in range(N):
    x = int(sys.stdin.readline().strip())
    arr.append(x)
    tmp +=x
    sum.append(tmp)

dp = [[0]*(M+1) for _ in range(N+1)]
check = [[False]*(M+1) for _ in range(N+1)]

def solve(n,m):
    
    if m==0:
        return 0
    if n<0:
        return -1e9
    if check[n][m]:
        return dp[n][m]

    dp[n][m] = solve(n-1,m)

    for k in range(n,0,-1):
        tmp = solve(k-2,m-1) + sum[n] - sum[k-1]
        dp[n][m] = max(dp[n][m], tmp)
        pass

    check[n][m] = True
    return dp[n][m]
    
    pass

print(solve(N,M))

