
import sys

N, M = map(int, sys.stdin.readline().split())

map1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*(M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        dp[i][j] = map1[i][j]
        if j!=0:
            dp[i][j] +=dp[i][j-1]
            pass

for i in range(N):
    for j in range(M):
        if i!=0:
            dp[i][j] +=dp[i-1][j]
            pass

K = int(sys.stdin.readline())
#print(dp)
l_result = []
for _ in range(K):
    ques = list(map(int, sys.stdin.readline().split()))
    a= ques[0]-1; b=ques[1]-1; c=ques[2]-1; d=ques[3]-1
    result = dp[c][d] #- dp[c-1][d] - dp[a][b-1] + dp[a-1][b-1]
    
    if b-1>=0:
        result -= dp[c][b-1]
        #print(">1")
    if a-1>=0:
        result -= dp[a-1][d]
        #print(">2")
    if a-1>=0 and b-1>=0:
        result += dp[a-1][b-1]
        #print(">3")
    l_result.append(result)

for e in l_result:
    print(e)

