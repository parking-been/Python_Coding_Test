import sys

N = int(sys.stdin.readline().strip())

array = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(21) for _ in range(N+1)]

dp[0][array[0]] = 1

for i in range(1,N-1):
    for j in range(0,21):
        if dp[i-1][j]>0:
            if 0<=j-array[i]<=20:
                dp[i][j-array[i]] +=dp[i-1][j]
            if 0<=j+array[i]<=20:
                dp[i][j+array[i]]+=dp[i-1][j]
            pass
        pass

print(dp[N-2][array[N-1]])