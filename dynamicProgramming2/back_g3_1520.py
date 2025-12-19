import sys
sys.setrecursionlimit(10**7)
from collections import deque
H, W = map(int, sys.stdin.readline().split())

world = []
move = [[-1,0],[0,-1],[1,0],[0,1]]
def dfs(x,y):
    
    if x==H-1 and y==W-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]

    dp[x][y]=0
    for m in move:
        nx, ny = x+m[0], y+m[1]
        if 0<=nx<H and 0<=ny<W and world[nx][ny]<world[x][y]:
            dp[x][y]+=dfs(nx, ny)
    
    return dp[x][y]
    
    pass


for i in range(H):
    arr = list(map(int, sys.stdin.readline().split()))
    world.append(arr)

dp = [[-1]*W for _ in range(H)]
print(dfs(0,0))