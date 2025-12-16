import sys

N = int(sys.stdin.readline().strip())
num = [0]
dp = [0]*(N+1)

for i in range(N):
    num.append(int(sys.stdin.readline().strip()))
    pass


maxi = 1
for i in range(1,N+1):
    for j in range(i):
        if num[i]>=num[j]:
            dp[i] = max(dp[j]+1, dp[i])
        pass
    maxi = max(dp[i], maxi)

print(N-maxi)