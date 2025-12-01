import sys
import copy
from collections import deque
move1 = [[0,1],[-1,0]]
move2 = [[0,-1],[-1,0]]


N, M = map(int, sys.stdin.readline().split())
world = []

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    world.append(arr)

dp1 = copy.deepcopy(world)
dp2 = copy.deepcopy(world)

def bfs(dp,move, x,y):
    visited = [[False]*(M) for _ in range(N)]
    q = deque()
    q.append((x,y))
    while q:
        curx, cury = q.popleft()
        for m in move:
            nx = curx + m[0]
            ny = cury + m[1]
            if 0<=nx<N and 0<=ny<M :
                if not visited[nx][ny]:
                    tmp = world[nx][ny] + dp[curx][cury]
                    dp[nx][ny] = tmp
                    q.append((nx,ny))
                    visited[nx][ny] = True
                else:
                    tmp = world[nx][ny] + dp[curx][cury]
                    dp[nx][ny] = max(tmp,dp[nx][ny])                
            pass
        
        pass
    
    pass


bfs(dp1,move1, N-1,0)

bfs(dp2,move2, N-1, M-1)

result = -int(1e9)
for i in range(N):
    for j in range(M):
        result = max(result, dp1[i][j] + dp2[i][j])
print(result)
