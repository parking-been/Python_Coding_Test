import sys


move= [[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
check_side = [[-1,-1],[-1,1],[1,1],[1,-1]]
N, M = map(int ,sys.stdin.readline().split())

first = [[N-1,1-1],[N-1,2-1],[N-1-1,1-1],[N-1-1,2-1]]

world = []

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    world.append(arr)

def make_cloud(i):
    cloud = []
    if i==0:
        cloud = first
        pass
    else:
        #world 에서 2 이상인 칸에 구름 이때 이전칸과 겹치지 않도록
        for a in range(N):
            for b in range(N):
                if world[a][b]>=2 and (a,b) not in after_set:
                    cloud.append([a,b])
                    world[a][b]-=2
        pass
    return cloud   

def move_cloud(d,s):
    dx = move[d][0]
    dy = move[d][1]
    after = []
    for c in cloud:
        nx = (c[0] + dx*s)%N 
        ny = (c[1] + dy*s)%N
        after.append([nx, ny])
    
    return after

def watering():
    for a in after:
        world[a[0]][a[1]] +=1
        pass
    pass

def update_water():
    for a in after:
        count = 0
        for c in check_side:
            nx = a[0] + c[0]
            ny = a[1] + c[1]
            if 0<=nx<N and 0<=ny<N and world[nx][ny]>0:
                count+=1
        world[a[0]][a[1]]+=count

    pass


for i in range(M):
    d,s = map(int, sys.stdin.readline().split())
    
    cloud = make_cloud(i)

    after = move_cloud(d,s)
    after_set = set((x,y) for x,y in after)

    watering()
    update_water()

cloud = make_cloud(M)
sum=0
for w in world:
    for c in w:
        sum+=c

print(sum)

    
    

    
