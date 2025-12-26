import sys

N, M, K = map(int, sys.stdin.readline().split())

flight = dict()

for i in range(K):
    a, b, c = map(int, sys.stdin.readline().split())
    if (a,b) in flight.keys():
        c = max(flight[(a,b)], c)
    flight[(a,b)] = c
    pass

dp = [[0]*(N+1) for _ in range(M)]

for i in range(2,N+1):
    dp[1][i] = -1
    if (1,i) in flight.keys():
        dp[1][i] = max(dp[1][i], flight[(1,i)])

for i in range(2,M):
    for j in range(i+1, N+1):
        dp[i][j]=-1
        for k in range(j-1,i-1,-1):
            #print("디버깅중입니다.",k)
            if dp[i-1][k]!=-1 and (k,j) in flight.keys():
                dp[i][j] = max(dp[i][j],dp[i-1][k]+flight[(k,j)])
            pass

#print(dp)

maxi = -1
for i in range(M):
    maxi = max(dp[i][N],maxi)
print(maxi)














# test = dict()
# test[(1,1)] = 1

# print(test)

# print((1,1) in test.keys())