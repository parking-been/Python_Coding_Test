import sys

N = int(sys.stdin.readline().strip())

array = list(map(int,sys.stdin.readline().split()))

total = sum(array)

dp = [0]*(N)
dp[0] = array[0]
for i in range(1, N):
    dp[i] = array[i] + dp[i-1]
maxi = 0

#case1 : 벌통 왼 끝 고정

for i in range(1,N-1):
    tmp_result = (total-array[-1]-array[i]) + dp[i-1]
    maxi = max(tmp_result, maxi)
    
#case2 : 벌통 오른 끝으로 고정

for i in range(1,N-1):
    tmp_result = (total-array[0]-array[i]) + (total - dp[i])
    maxi = max(tmp_result, maxi)

#case3
for i in range(1,N-1):
    tmp_result = total - array[0] - array[-1] + array[i]
    maxi = max(tmp_result, maxi)

print(maxi)