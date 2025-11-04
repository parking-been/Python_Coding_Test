import sys
from itertools import product
import copy
sys.setrecursionlimit(1_000_000) 
move = [[-1,0],[0,-1],[1,0],[0,1]]
rules = [[],
         [[0],[1],[2],[3]],
         [[0,2],[1,3]],
         [[0,1],[1,2],[2,3],[0,3]],
         [[0,1,2],[1,2,3],[1,0,3],[2,0,3]],
         [[0,1,2,3]]]

N, M = map(int, sys.stdin.readline().split())

world = []
cctv = []
for i in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    world.append(array)
    for j in range(M):
        if array[j]!=0 and array[j]!=6:
            cctv.append((i,j))
    pass


def solution(tboard, dir, x,y):
    
    for dd in dir :
        tx = x
        ty = y
        dx, dy = move[dd]
        
        while True:
            if 0<=tx<N and 0<=ty<M:
                if tboard[tx][ty]==0:
                    tboard[tx][ty] = -1
                if tboard[tx][ty] == 6:
                    break
                tx +=dx
                ty +=dy
                pass
            else:
                break

    pass

dataa = [0,1,2,3]

def check(board):
    count=0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                count+=1
    return count

def dfs(depth,borad):
    global mini
    if depth ==len(cctv):
        
        mini = min(mini,check(borad))

        # for ele in borad:
        #     print(ele)
        # print("~~~~~~~~~")
        return
    tmp_board = copy.deepcopy(borad)
    #탐색할 cctv
    x,y = cctv[depth]
    cas = world[x][y]
    for i in rules[cas]:
        solution(tmp_board, i, x, y)
        dfs(depth+1,tmp_board)
        tmp_board = copy.deepcopy(borad)

mini = int(1e9)
dfs(0,world)
print(mini)

#data = [0,1,2,3,4]
#print(list(product(data, repeat=3)))
