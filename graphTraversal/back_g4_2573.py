import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

move = [[-1,0],[0,-1],[1,0],[0,1]]
board = [[0]*M for _ in range(N)]

bing = []

for i in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if array[j]!=0:
            board[i][j] = array[j]
            bing.append([i,j])

def melt():
    melting = []
    for ele in bing:
        side = 0
        for m in move:
            x = m[0] + ele[0]
            y = m[1] + ele[1]
            if board[x][y]==0 : side +=1
        melting.append(board[ele[0]][ele[1]]-side)

    delete_list = []
    for idx, ele in enumerate(bing):
        #print(board[ele[0]][ele[1]])
        if melting[idx]>0:
            board[ele[0]][ele[1]] = melting[idx]
        else:
            board[ele[0]][ele[1]] = 0
            delete_list.append(idx)

    
    count = 0
    for idx in delete_list:
        bing.pop(idx-count)
        count +=1
    
    pass

def checkboard():
    visited =[[False]*M for _ in range(N)]
    q = deque()
    start = bing[0]
    visited[start[0]][start[1]] = True
    q.append(start)

    while q:
        cur = q.popleft()
        for m in move:
            x = cur[0] + m[0]
            y = cur[1] + m[1]
            if visited[x][y] == False and board[x][y]!=0:
                q.append([x,y])
                visited[x][y] = True
                
        pass
    
    

    for b in bing:
        if visited[b[0]][b[1]] ==False:
            #print("에러 발생 :", b)
            return True
    
    return False

    pass


count = 0
while len(bing)!=0:
    if(checkboard()):
        print(count)
        exit()
    
    melt()
    
    count +=1

    pass

print(0)
