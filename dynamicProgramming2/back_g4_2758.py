import sys
import math
from collections import deque
T = int(sys.stdin.readline().strip())



def solution(n,m):
    #1~m , n개
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[0][0] = 1
    for i in range(1,m+1):
        for j in range(0,n+1):
            if j==0:
                dp[i][j]=1
                continue
            #i이하의 수에서 j개 뽑기
            dp[i][j] = dp[i-1][j] + dp[i//2][j-1]
    
    print(dp[m][n])
    

for i in range(T):
    n, m = map(int,sys.stdin.readline().split())
    solution(n,m)
    
    pass

