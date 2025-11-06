import sys

T = int(sys.stdin.readline().strip())


def solution():
    dp  = [[0]*(M+1) for _ in range(N+1)] 
    
    for i in range(1,N+1):
        dp[i][0]=1
        pass

    for i in range(1,N+1):
        for j in range(1,M+1):
            dp[i][j] = dp[i-1][j] 
            if j-array[i-1]>=0:
                dp[i][j] += dp[i][j-array[i-1]]
            
            pass
    
    print(dp[N][M])
    


for _ in range(T):
    N = int(sys.stdin.readline().strip())
    array = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())

    solution()

    
    pass