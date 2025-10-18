import sys

T = int(sys.stdin.readline().strip())

def solution():
    N = int(sys.stdin.readline().strip())
    parent = [0]*(N+1)
    visited = [False]*(N+1)

    for _ in range(N-1):
        P, M = map(int, sys.stdin.readline().split())
        parent[M] = P
        pass

    p1, p2 = map(int, sys.stdin.readline().split())
    # visited[p1] = True
    # visited[p2] = True
    pn = p1
    pn2 = p2
    
    while pn!=0:
        visited[pn] = True
        pn = parent[pn]
    
    while True:
        if visited[pn2] == True:
            return pn2
        pn2 = parent[pn2]

    pass



for _ in range(T):
    print(solution())
    
    pass