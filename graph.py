from collections import defaultdict
from collections import deque
import sys

# 그래프 만들기
N,M = map(int, sys.stdin.readline().split())

G= defaultdict(list)

for _ in range(M):
    u,v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

#print(G)
#exit()




##dfs - 재귀로 구현
def dfs(start, visited=[False]*(N+1)):
    visited[start] = True
    print(start , end=" ")
    for v in G[start]:
        if not visited[v]:
            dfs(v, visited)
    return visited

##dfs - stack, for문으로 구현하기
def dfs2(start, visited=[False]*(N+1)):
    stack = deque()
    stack.append(start)
    while stack:
        v=stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")
            for u in G[v]:
                stack.append(u)
    return visited

##bfs 구현하기 
#queue는append 는 똑같으나,  popleft 사용해야함 주의
def bfs(start, visited=[False]*(N+1)):
    que = deque()
    que.append(start)
    while que:
        v = que.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")
            for u in G[v]:
                que.append(u) 


dfs(1) #1243
dfs2(1) #1432
bfs(1) #1234

"""
입력값
4 5
1 2
1 3
1 4
2 4
3 4

"""