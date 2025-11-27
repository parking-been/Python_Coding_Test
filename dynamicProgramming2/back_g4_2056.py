import sys

N = int(sys.stdin.readline().strip())

time = [0]*(N+1)
dp = [0]*(N+1)
for i in range(1,N+1):
    arr = list(map(int, sys.stdin.readline().split()))
    time[i] = (arr[0])
    leng = arr[1]
    prelist = arr[2:]
    
    if leng ==0:
        dp[i]=time[i]
    else:
        max_prev = 0
        for ele in prelist:
            max_prev = max(max_prev, dp[ele])
        dp[i] = max_prev + time[i]

print(max(dp))

    
    
    

