import sys

N, M = map(int, sys.stdin.readline().split())


pan = list(map(int, sys.stdin.readline().split()))

# 두개의 웤 어떻게 병행할지 고민했는데
# set을 사용하면 된다!
# 웤 하나만 사용하는 경우
pan_set = set(pan)
# 웤을 두개 동시에 사용하는 경우
for i in range(M):
    for j in range(i+1, M):
        pan_set.add(pan[i]+pan[j])

dp = [1e9]*(N+1)

dp[0] = 0

for pp in pan_set:
    for j in range(pp,N+1):    
        tmp = j-pp
        if dp[tmp]!=1e9:
            dp[j] = min(dp[j], dp[tmp]+1)
        pass

result=dp[N]
if result == 1e9:
    print(-1)
else:
    print(result)