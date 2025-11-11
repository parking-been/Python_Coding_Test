import sys
from collections import deque

move = [[-1,0],[0,-1],[1,0],[0,1]]

N, K = map(int, sys.stdin.readline().split())

world = []
virous = [[] for _ in range(K+1)]

for i in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    world.append(array)
    for j in range(N):
        if array[j]!=0:
            virous[array[j]].append((i,j))

S, X, Y = map(int, sys.stdin.readline().split())

def bfs(depth):
    q= deque()
    visited = [[False] * N for _ in range(N)]
    
    
    for eles in virous:
        for i in eles:
            q.append(i)
            visited[i[0]][i[1]] = True


    
    nextq = deque()
    for _ in range(depth):

        while q:
            curx, cury = q.popleft()
            state = world[curx][cury]
            
            for m in move:
                nx = curx + m[0]
                ny = cury + m[1]
                if 0<=nx<N and 0<=ny<N:
                    if world[nx][ny]==0 and not visited[nx][ny]: 
                        visited[nx][ny] = True
                        world[nx][ny] = state
                        # print(nx, ny)
                        # print(state)
                        # print(world)
                        # exit()
                        nextq.append(((nx,ny)))
            pass
        q = nextq

        # print("~~디버깅")
        # for ele in world:
        #     print(ele)
        

    pass

bfs(S)
print(world[X-1][Y-1])

