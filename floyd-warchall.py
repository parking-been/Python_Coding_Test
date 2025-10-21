import sys

INF = int(1e9)

#노드의 개수 간선의 개수 입력 받기
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신에서 자기자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

#각 간선에서 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    #a에서 b로 가는 비용은 c 라고 설정
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한 (INFINITY) 라고 출력
        if graph[a][b]==INF:
            print("INFINITY", end="")
        else:
            print(graph[a][b], end="")
    print()