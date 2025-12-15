import sys

coin = []

T = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
dp = [[0]*(T+1) for _ in range(k+1)]

for i in range(k):
    p,n = map(int,sys.stdin.readline().split())
    coin.append((p,n))
    dp[i][0] = 1
dp[k][0] = 1

coin.sort()


total = 0

for i in range(k):
    
    cur,cc = coin[i]
    c = i+1
    for j in range(1,T+1):
        for m in range(min(cc, j//cur)+1):

            if j-m*cur>=0:
                dp[c][j] += dp[c-1][j-m*cur]
            

print(dp[k][T])

        
    
    
        



