import sys
from collections import deque
M,N,H = map(int, sys.stdin.readline().split())

box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
move = [[-1,0,0],[0,-1,0],[0,0,-1],[1,0,0],[0,1,0],[0,0,1]]
#print(box[0])

queue = deque()
visited = [[[False]*(M)for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k]==1:
                queue.append((i,j,k))
                box[i][j][k]=0
                visited[i][j][k] = True



def bfs(queue, visited):
    max_r = 0
    while queue : 
        cur = queue.popleft()
        dis = box[cur[0]][cur[1]][cur[2]]
        for e in move:
            x = cur[0] + e[0]
            y = cur[1] + e[1]
            z = cur[2] + e[2]

            if(0<=x<H and 0<=y<N and 0<=z<M):
                if((not visited[x][y][z]) and box[x][y][z]==0):
                    queue.append((x,y,z))
                    box[x][y][z] = dis+1
                    max_r = max(dis+1, max_r)
        pass
    pass
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k]==False and box[i][j][k]==0:
                    print(-1)
                    return
    print(max_r)
    return

bfs(queue, visited)

