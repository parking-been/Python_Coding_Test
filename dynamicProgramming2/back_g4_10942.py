import sys

N = int(sys.stdin.readline().strip())

array = [-1] + list(map(int, sys.stdin.readline().split()))

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(N+1):
        if i==1:
            dp[i][j]=1
            continue
        if i==2 and j<N:
            if array[j] == array[j+1]:
                dp[i][j]=1
                continue

        if i+j-1<=N:
            if dp[i-2][j+1]==1 and array[j] == array[i+j-1]:
                dp[i][j]=1
        
        pass

T = int(sys.stdin.readline().strip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b-a+1][a])