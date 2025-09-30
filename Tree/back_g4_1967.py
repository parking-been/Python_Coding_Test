import sys
from collections import defaultdict, deque
n = int(sys.stdin.readline())

graph = defaultdict(list)
for i in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    graph[p].append((c,w))
    graph[c].append((p,w))


def bfs(start):
    visited=[False]*(n+1)
    count = [0]*(n+1)
    que = deque()
    que.append(start)
    m = 0
    idx = -1
    visited[start] = True
    while que:
        cur = que.popleft()
        #weight = cur[1]
        dis = count[cur]
        #print("c",cur,"dis", dis)
        
        for e in graph[cur]:
            if not visited[e[0]]:
                que.append(e[0])
                count[e[0]] = dis + e[1]
                visited[e[0]]=True
                if m< count[e[0]]:
                    m = count[e[0]]
                    idx = e[0]
                    
                pass
    #print(idx, m)
    return idx, m

idx, m= bfs(1)
r_idx, r_m = bfs(idx)

print(r_m)