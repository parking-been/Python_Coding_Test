import sys
import heapq
N, M, K, X = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1)

for _ in range(M):
    a, b= map( int, sys.stdin.readline().split())
    graph[a].append(b) #a-> b 단방향

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    dis[start] = 0

    while q :
        d, cur = heapq.heappop(q)
        if dis[cur] < d:
            continue
        for nt in graph[cur]:
            cost = d + 1
            if cost < dis[nt]:
                dis[nt] = cost
                heapq.heappush(q, (cost, nt))
        
        pass
    pass

dijkstra(X)

result = []
for i in range(1,N+1):
    if dis[i] == K:
        result.append(i)

if len(result) == 0 : 
    print(-1)
else :
    for e in result: print(e )


