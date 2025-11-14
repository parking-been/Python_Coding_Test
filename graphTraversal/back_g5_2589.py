import sys
from collections import deque
move = [[-1,0],[0,-1],[1,0],[0,1]]

N,M = map(int,sys.stdin.readline().split())

world = []
Llist = []
for i in range(N):
    array = list(sys.stdin.readline().strip())
    world.append(array)
    for j in range(M):
        if array[j] == 'L':
            Llist.append((i,j))
    pass


def bfs(j,k):
    q = deque()
    visited = [[False]*(M) for _ in range(N)]
    q.append((j,k,0))
    visited[j][k] = True

    while q:
        curx, cury, dis = q.popleft()
        global result 
        result = max(result, dis)
        for m in move:
            x = curx + m[0]
            y = cury + m[1]
            if 0<=x<N and 0<=y<M :
                if not visited[x][y] and world[x][y]=='L':
                    q.append((x,y,dis+1))
                    visited[x][y] = True

        pass
    pass

result = 0

for j,k in Llist:
    bfs(j,k)
    pass
print(result)