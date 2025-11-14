import sys

S = sys.stdin.readline().strip()
M = int(sys.stdin.readline().strip())


world = []

for i in range(M):
    a, b = sys.stdin.readline().split()
    world.append((a,int(b)))

dp = [[0]*(len(S)+1) for _ in range(len(world)+1)]
dp2 = [0]*(len(S)+1)
for j in range(len(S)+1):
    
    
    for i in range(len(world)+1):
        if i==0:
            dp[i][j]=j
            continue
        if j==0:
            dp[i][j]=0
            continue
        target = world[i-1][0]
        lengg = len(target)
        weight = world[i-1][1]
        
        flag = 1 # 포함 된다.
        dp[i][j] = max(dp[i][j], dp2[j-1]+1)
        
        if (j-lengg)<0:
            flag = 0
        
        if S[j-lengg:j] != target:
            flag = 0 
            

        if flag==1:
            #print("디버깅", i,j)
            dp[i][j] = dp2[j-lengg] + weight

        #tmp = max(dp2[j-1]+1, dp[i-1][j])
        dp[i][j] = max(dp[i][j], dp2[j-1]+1)

        dp2[j] = max(dp2[j], dp[i][j])
#print(dp)
print(dp2[len(S)])
        
        