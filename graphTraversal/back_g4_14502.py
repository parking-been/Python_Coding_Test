import sys
from collections import deque
from itertools import combinations
import copy
move = [[-1,0],[0,-1],[1,0],[0,1]]

N, M = map(int, sys.stdin.readline().split())

world = []
empty = []
for i in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    world.append(array)
    for j in range(M):
        if array[j]==0:
            empty.append((i,j))
totalresult = 0

def bfs():
    # 유효 영역 확인하기
    
    q = deque()
    for i in range(N):
        for j in range(M):
            if cworld[i][j] ==2:
                q.append((i,j))

    while q:
        cur = q.popleft()
        for m in move:
            cx = cur[0] + m[0]
            cy = cur[1] + m[1]
            if 0<=cx<N and 0<=cy<M:
                if cworld[cx][cy] == 0 :
                    q.append((cx,cy))
                    cworld[cx][cy] = 2
                    

    cnt =0
    for i in range(N):
        for j in range(M):
            if cworld[i][j]==0:
                cnt+=1
    global totalresult
    totalresult = max(cnt, totalresult)
    pass

   

for walls in combinations(empty,3):
    cworld = copy.deepcopy(world)
    for wall in walls:
        x = wall[0]
        y = wall[1]
        cworld[x][y] = 1
    bfs() 

print(totalresult)