import sys

s1_sq = sys.stdin.readline().strip()
s2_sq = sys.stdin.readline().strip()

M = len(s1_sq)
N = len(s2_sq)

dp = [[0]*(M+1) for _ in range(N+1)] 

for i in range(1,N+1): #s2
    for j in range(1, M+1): #s1
        if s2_sq[i-1] == s1_sq[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
            pass
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            pass

        pass

print(dp[N][M])