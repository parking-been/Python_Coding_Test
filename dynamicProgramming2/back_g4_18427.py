import sys
from collections import defaultdict
C = 10007
N,M,H = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for i in range(N):
    arr = map(int, sys.stdin.readline().split())
    for ele in arr:
        graph[i].append(ele)
    pass


dp = [[0]*(H+1) for _ in range(N)]

for i in range(N):
    dp[i][0]=1

for j in graph[0]:
    dp[0][j] = 1

for i in range(1,N):
    for j in range(1, H+1):
        
        dp[i][j] = dp[i-1][j]
        for e in graph[i]:
            if (j-e)>=0 and i-1>=0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-e])%C
        
        pass
    
    
print(dp[N-1][H]%C)