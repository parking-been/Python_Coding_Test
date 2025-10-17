import sys

N, K = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    ele = list(map(int,sys.stdin.readline().split()))
    array.append(ele)

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        w = array[i-1][0]
        v = array[i-1][1]
        
        if j<w: # 가방에 못 넣는 경우
            dp[i][j] = dp[i-1][j]
            pass
        else: #넣을 수 있는 경우
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
            pass
        pass

print(dp[N][K])