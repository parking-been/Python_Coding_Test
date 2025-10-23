import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
move = [[-1,0],[0,-1],[1,0],[0,1]]

world = []
aircons = []
visited = [[False]*(M) for _ in range(N)]


for j in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    
    for i in range(M):
        if row[i] == 9:
            aircons.append((j,i))
            visited[j][i] = True
    world.append(row)
    pass


def bfs():
    q = deque()
    for e in aircons:
        q.append(e)
    while q:
        c, r = q.popleft()
        for m in move:
            dx = m[0]
            dy = m[1]
            x = c + dx
            y = r + dy
            while 0<=x<=N-1 and 0<=y<=M-1:
                visited[x][y]=1
                state = world[x][y]
                if state ==9:
                    break
                if state == 3:
                    dx, dy = -dy, -dx
                elif state == 4:
                    dx, dy = dy, dx
                elif (state == 1 and dx==0) or(state ==2 and dy==0):
                    break
                x +=dx
                y +=dy
                pass
    count = 0
    for ans in visited:
        count+=ans.count(1)
    print(count)

    pass

bfs()