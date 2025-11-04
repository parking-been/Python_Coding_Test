import sys

N, M = map(int,sys.stdin.readline().split())

world = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    world[b][a] = 1

for i in range(2,N+1):
    for j in range(1,N+1):
        if world[i][j]==1:
            p = max(world[j])
            world[i][j] = p+1

for i in range(1,N+1):
    print(max(world[i])+1, end = ' ')