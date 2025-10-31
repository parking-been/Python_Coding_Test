import sys
from collections import deque
move = [[-1,0],[0,-1],[1,0],[0,1]]

N,M = map(int,sys.stdin.readline().split())

world = []

cheese = []
c_count = 0
for i in range(N):
    array = list(map(int,sys.stdin.readline().split()))
    world.append(array)
    for j in range(M):
        if array[j]==1:
            c_count+=1
            cheese.append((i,j))
            

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        cur = q.popleft()
        for m in move:
            x = cur[0] + m[0]
            y = cur[1] + m[1]
            if 0<=x<N and 0<=y<M and not visited[x][y] and world[x][y]==0:
                q.append((x,y))
                visited[x][y] = True

def checkMelt():
    
    for ch in cheese:
        for m in move:
            x = m[0] + ch[0]
            y = m[1] + ch[1]
            if 0<=x<N and 0<=y<M:
                if world[x][y] ==0 and visited[x][y]:
                    deletelist.append((ch[0],ch[1]))
                    break
        pass

    pass

def melting():
    for ele in deletelist:
        world[ele[0]][ele[1]] = 0
    pass

def checkCheese():
    for i in range(N):
        for j in range(M):
            if world[i][j]==1:
                cheese.append((i,j))
    
round = 0
last = 0
p_count = c_count
while c_count!=0:
    visited = [[False]*(M) for _ in range(N)]
    bfs(0,0)
    deletelist = []
    checkMelt()
    melting()
    round+=1
    cheese = []
    checkCheese()
    p_count = c_count
    c_count = len(cheese)

    

print(round)
print(p_count)
    
