import sys
from collections import deque
move = [(-1,2),(1,6)]

world = []

for i in range(4):
    world.append(deque(list(map(int,sys.stdin.readline().strip()))))


T = int(sys.stdin.readline().strip())

def check(n,d):
    total = []
    total.append((n,d))
    visited = [False]*4
    q = deque()
    q.append((n,d))
    visited[n] = True

    while q:
        cur,dir = q.popleft()
        for m,p in move:
            x = cur+m
            if 0<=x<4 and not visited[x]:
                if world[x][p]!=world[cur][8-p]:
                    q.append((x,-dir))
                    total.append((x,-dir))
                    visited[x] = True
        pass
    return total
    pass

def update(arr):

    for n,d in arr:
        if d==-1:
            cur = world[n].popleft()
            world[n].append(cur)
        else:
            cur = world[n].pop()
            world[n].appendleft(cur)
            pass
        
    pass

def calculate():
    sum = 0
    if world[0][0] == 1:
        sum+=1
    if world[1][0] == 1:
        sum+=2
    if world[2][0] == 1:
        sum+=4
    if world[3][0] == 1:
        sum+=8
    return sum
    pass

for i in range(T):
    N, D = map(int,sys.stdin.readline().split())
    change = check(N-1,D)
    update(change)
    
    pass

print(calculate())