import sys

from collections import defaultdict, deque
K = int(sys.stdin.readline().strip())



def bfs(start):
    q = deque()
    q.append((start,'r'))
    visited[start] = 'r'
    ani = 'b'

    while q:
        cur, col = q.popleft()

        if col=='r':
            ani = 'b'
            
        else:
            ani = 'r'
        
        for j in graph[cur]:
            if visited[j]=='':
                q.append((j,ani))
                visited[j] =ani
                pass
            else:
                if visited[j]==col:
                    return False

        #print(visited)
        pass

    return True
    pass


for i in range(K):
    
    graph = defaultdict(list)
    
    V, E = map(int, sys.stdin.readline().split())

    for j in range(E):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        pass
    
    visited = ['']*(V+1)
    result = True
    for k in range(1,V+1):
        if visited[k]=='':
            result = bfs(k)
            if result == False:
                break
    
    if result:
        print("YES")
    else:
        print("NO")