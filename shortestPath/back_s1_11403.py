import sys
INF = int(1e9)
N = int(sys.stdin.readline().strip())

world = []

for i in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if array[j]==0:
            array[j] = INF
    world.append(array)
    pass

for k in range(N):
    for a in range(N):
        for b in range(N):
            world[a][b] = min(world[a][b] , world[a][k]+world[k][b])

for i in range(N):
    for j in range(N):
        #if i==j : print(1, end=" ")
        if world[i][j]>=1 and world[i][j]!=INF: print(1, end=" ")
        else : print(0, end=" ")
    print()