import sys

T = int(sys.stdin.readline().strip())

def find(parent, x):
    #x의 루트 찾기
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])
    pass

def Union(parent,a,b):
    pa = find(parent,a)
    pb= find(parent, b)
    if pa!=pb : parent[max(pa,pb)] = min(pa,pb)

for i in range(1,T+1):
    V = int(sys.stdin.readline().strip())
    parent = [j for j in range(V)]
    
    E = int(sys.stdin.readline().strip())
    for _ in range(E):
        a, b = map(int,sys.stdin.readline().split())
        if (a!=b):
            Union(parent, a,b)
        pass
    
    M = int(sys.stdin.readline().strip())

    print(f"Scenario {i}:")

    for _ in range(M):
        a, b = map(int,sys.stdin.readline().split())
        if (find(parent,a)==find(parent,b)):
            print(1)
        else:
            print(0)
        pass
    
    print()
    pass