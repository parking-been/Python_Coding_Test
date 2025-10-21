import heapq
import sys

INF = int(1e9) #무한을의미하는 값

n, m = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]

distance = [INF]*(n+1)

#모든 간선의 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    #
    graph[a].append((b,c))
    graph[b].append((a,c))

    pass

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #(거리, 노드)
    distance[start] = 0
    while q:
        dist , now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

    pass

dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력 
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])