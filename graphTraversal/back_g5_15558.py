import sys
from collections import deque

N, k = map(int, sys.stdin.readline().split())

move = [[0,1],[0,-1],[1,k]]

world = []
st = [int(x) for x in sys.stdin.readline().strip()]
world.append(st)
st2 = [int(x) for x in sys.stdin.readline().strip()]
world.append(st2)


def bfs(i,j):
    q = deque()
    q.append((i,j,0))
    visited = [[False] * N for _ in range(2)]
    visited[0][0] = True
    while q:

        cx, cy, time = q.popleft()
        
        if cy<time:
            continue

        for m in move:
            x = (cx + m[0])%2
            y = (cy + m[1])
            if y >= N :
                return 1
            if 0<=y<N:
                if world[x][y]==1 and not visited[x][y]:
                    visited[x][y] = True
                    q.append((x,y,time+1))
            
    return 0

    pass

print(bfs(0,0))