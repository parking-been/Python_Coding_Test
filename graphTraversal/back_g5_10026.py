import sys
from collections import deque
N = int(sys.stdin.readline().strip())
world = []
move = [[-1,0],[0,-1],[1,0],[0,1]]
for i in range(N):
    arr = list(sys.stdin.readline().strip())
    world.append(arr)

def bfs(x,y,count):
    this = world[x][y]
    q = deque()
    q.append((x,y))
    visited[x][y] = count
    while q:
        curx, cury = q.popleft()
        
        for m in move:
            nx = curx+m[0]
            ny = cury+m[1]
            if 0<=nx<N and 0<=ny<N:
                
                if world[nx][ny]==this and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny] = count


count = 1
visited = [[0]*(N) for i in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0 :
            bfs(i,j,count)
            count+=1 

for i in range(N):
    for j in range(N):
        if world[i][j]=='G':
            world[i][j]='R'

ttcount = 1
visited = [[0]*(N) for i in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0 :
            bfs(i,j,ttcount)
            ttcount+=1



print(count-1, ttcount-1) 