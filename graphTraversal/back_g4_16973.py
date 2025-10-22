import sys
from collections import deque

move = [[-1,0],[0,-1],[1,0],[0,1]]
N, M = map( int, sys.stdin.readline().split())

world = [[0]*(M+1)]
visited = [[False]*(M+1) for _ in range(N+1)] # 필요 없을 것 같다
block = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    array = [0] + list(map(int, sys.stdin.readline().split()))
    world.append(array)

for i in range(1,N+1):
    tmp = 0
    for j in range(1,M+1):
        tmp +=world[i][j]
        block[i][j] = tmp + block[i-1][j]
        pass


H,W,Sr,Sc,Fr,Fc = list(map(int,sys.stdin.readline().split()))
def blocked(r,c):
    r2 = r+H-1
    c2 = c+W-1
    if r < 1 or c < 1 or r2 > N or c2 > M:
        return True
    s = block[r2][c2] - block[r-1][c2] - block[r2][c-1] + block[r-1][c-1]
    return s > 0
    pass

def bfs():
    q = deque()
    q.append((Sr,Sc,0))
    while q:
        Cr, Cs, time = q.popleft()
        if Cr == Fr and Cs == Fc:
            return time
        
        for m in move:
            Nr = m[0] + Cr
            Nc = m[1] + Cs

            if 1<=Nr<=N-H+1 and 1<=Nc<=M-W+1 and not visited[Nr][Nc]:
                flag = blocked(Nr,Nc)
                
                if flag==0:
                    q.append((Nr,Nc, time+1))
                    
                    visited[Nr][Nc] = True  
                
                pass 
            else: continue

            pass

        pass   
    return -1    
    pass

print(bfs())