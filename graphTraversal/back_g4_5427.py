import sys
from collections import deque
move = [[-1,0],[1,0],[0,-1],[0,1]]


T = int(sys.stdin.readline().strip())


def bfs(x,y,t):

    if x == 0 or x == H-1 or y == 0 or y== W-1:
        return 1
    q = deque()
    q.append((x,y,t))
    svisited[x][y] = True
    while q:
        cx, cy, ct = q.popleft()

        for m in move:
            nx = cx + m[0]
            ny = cy + m[1]
            nt = ct + 1
            if 0<=nx<H and 0<=ny<W and world[nx][ny]!='#'and (nt<visited[nx][ny] or visited[nx][ny]==-1) and not svisited[nx][ny]:
                if nx == 0 or nx == H-1 or ny == 0 or ny== W-1:
                    return nt+1
                q.append((nx,ny,nt))
                visited[nx][ny] = True

    return -1


def burn():

    for f in fires:
        visited[f[0]][f[1]] = 0

    while fires:
        x,y,t = fires.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if 0<=nx<H and 0<=ny<W and world[nx][ny] !='#' and visited[nx][ny]==-1:
                visited[nx][ny] = t+1
                fires.append((nx,ny,t+1))
        pass
    pass

for i in range(T):
    sang = [0,0]
    fires = deque()
    W,H = map(int, sys.stdin.readline().split())
    world = []
    visited = [[-1]*(W) for _ in range(H)]
    svisited = [[False]*(W) for _ in range(H)]
    for h in range(H):
        arr = list(sys.stdin.readline().strip())
        for w in range(W):
            if arr[w] == '@':
                sang = [h,w]
            elif arr[w] == '*':
                fires.append((h,w,0))
        world.append(arr)
    
    
    burn()
    

    result = bfs(sang[0],sang[1],0)
    if result==-1:
        print("IMPOSSIBLE")
    else:
        print(result)

    pass