import sys
n, k = map(int, sys.stdin.readline().split())

coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

coin.sort()
#print(coin)
list = []
dp = [0]*(k+1)
dp[0]=1
for c in coin:
    for i in range(c,k+1):
        dp[i]+=dp[i-c]

print(dp[k])