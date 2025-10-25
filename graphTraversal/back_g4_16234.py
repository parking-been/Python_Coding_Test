import sys
from collections import deque

move = [[-1,0],[0,-1],[1,0],[0,1]]

N, L, R = map(int, sys.stdin.readline().split())

world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))


def bfs(x,y):
    total_loc = []
    sum = 0
    q = deque()
    q.append((x,y))
    total_loc.append((x,y))
    sum+=world[x][y]
    visited[x][y] = True
    while q:    
        cx, cy = q.popleft()
        cval = world[cx][cy]
        for m in move:
            tx = cx + m[0]
            ty = cy + m[1]
            if 0<=tx<N and 0<=ty<N and not visited[tx][ty]:
                if L<=abs(cval-world[tx][ty])<=R:
                    q.append((tx,ty))
                    total_loc.append((tx,ty))
                    sum+=world[tx][ty]
                    visited[tx][ty] = True

        pass
    
    eachval = int(sum/len(total_loc))

    for tmp in total_loc:
        world[tmp[0]][tmp[1]] = eachval
    
    if len(total_loc)==1:
        return 0
    else:
        return 1
    
    pass

count = 0
while True:
    visited = [[False]*(N) for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                value = bfs(i,j)
                flag +=value
    
    
    if flag==0:
        break
    #print(world)
    count+=1
print(count)