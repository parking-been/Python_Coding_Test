import sys
INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())

move = [[-1,-1],[-1,0],[-1,1]]

world = []
dp = [[[INF]*(M) for _ in range(N)] for _ in range(3)] #0,n,m
for _ in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    world.append(array)

for j in range(M):
    dp[0][0][j]=world[0][j]
    dp[1][0][j]=world[0][j]
    dp[2][0][j]=world[0][j]


def solution(x,y):
    
    for idx,m in enumerate(move):
        cx = x + m[0]
        cy = y + m[1]
        if 0<=cx<N and 0<=cy<M:
            for i in range(3):
                if idx!=i:
                    dp[idx][x][y] = min(world[x][y]+dp[i][cx][cy], dp[idx][x][y])
            pass
    
    
    pass

for i in range(1,N):
    for j in range(M):
        solution(i,j)
    pass

mint = INF
for j in range(M):
    for i in range(3):
        mint = min(dp[i][N-1][j],mint)

print(mint)

