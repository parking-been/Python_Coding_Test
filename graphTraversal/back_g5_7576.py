import sys
from collections import deque 
M, N = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[-1,0],[0,-1],[1,0],[0,1]]
rotten = []

for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            rotten.append((i,j))


def bfs( rotten, visited = [[False]*(M) for _ in range(N)]):
    
    day = 0
    #queue = deque()
    curlist = []
    for e in rotten : 
        curlist.append(e)
        visited[e[0]][e[1]] = True
    while True:
        add_list = []
        for e in curlist:
            for m in move:
                x = e[0]+m[0]
                y = e[1] + m[1]
                
                if (x<0 or y<0 or x>=N or y>=M): continue
                if (not visited[x][y]) and box[x][y]==0 : 
                    visited[x][y] = True
                    add_list.append((x,y))
        
        
        if len(add_list)==0: break
        day+=1
        curlist = add_list
        
        pass
    
    for i in range(N):
        for j in range(M):
            if box[i][j]==0 and visited[i][j]==False:
                print(-1)
                return
            
    print(day)
    return
    
    
    


bfs(rotten)


