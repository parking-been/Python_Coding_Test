import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())

up = {}
snake = {}

for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    up[a] = b

for i in range(M):
    c,d = map(int,sys.stdin.readline().split())
    snake[c] = d

def bfs():
    visited = [False]*(101)
    q = deque()
    q.append((1,0))
    visited[1] = True
    
    while q:
        cur, time = q.popleft()
        for i in range(1,7):
            next = cur+i
            if next in up:
                next = up[next]
            elif next in snake:
                next = snake[next]
            if next ==100:
                return time+1
                break
            if 1<next<=100 and not visited[next]:
                visited[next] = True
                q.append((next, time+1))
            
                pass
    return -1    
    pass

print(bfs())