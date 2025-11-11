import sys

n,m = map(int ,sys.stdin.readline().split())
world = []
dp = [[0]*(m) for _ in range(n)]

for i in range(n):
    stirngg = sys.stdin.readline().strip()
    array = [int(s) for s in stirngg]
    world.append(array)

an = 0

for i in range(n):
    for j in range(m):
        if i==0 or j==0:
            dp[i][j] = world[i][j]
        
        elif world[i][j]==0:
            dp[i][j]=0
        else:
            dp[i][j]= min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        an = max(dp[i][j], an)

print(an*an)
