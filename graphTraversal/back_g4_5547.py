import sys
from collections import deque

move_o = [[0,-1],[-1,0],[0,1],[1,1],[1,0],[1,-1]]
move_e = [[-1,-1],[-1,0],[-1,1],[0,1],[1,0],[0,-1]]
W, H = map(int, sys.stdin.readline().split())
world = [[0]*(W+2)]

for i in range(H):
    array = [0]+list(map(int, sys.stdin.readline().split()))+[0]
    world.append(array)
    
world.append([0]*(W+2))


def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    visited = [[False]*(W+2) for _ in range(H+2)]
    count=0
    visited[sy][sx] = True
    while q:
        curx, cury = q.popleft()
        if cury%2==0:
            tmp = move_e
        else : 
            tmp = move_o
        for m in tmp:
            nx, ny = curx+m[0], cury+m[1]
            if 0<=nx<W+2 and 0<=ny<H+2:
                if not visited[ny][nx] and world[ny][nx]==0:
                    q.append((nx,ny))
                    visited[ny][nx] = True
                elif world[ny][nx]==1:
                    count+=1
    print(count)

bfs(0,0)