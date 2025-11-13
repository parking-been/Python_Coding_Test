import sys
import copy
D, P = map(int, sys.stdin.readline().split())

world = []
for i in range(P):
    L,C =  map(int, sys.stdin.readline().split())
    world.append((L,C))

    pass

world.sort()


dp = [0]*(D+1) 

for i in range(P):
    dp_pre = copy.deepcopy(dp)
    for j in range(1, D+1):
        #쓸 경우
        
        rest = j-world[i][0]
        if rest>0:
            if i-1>=0:
                dp[j] = min(dp_pre[rest],world[i][1])
            pass
        elif rest == 0:
            #print("디버깅중",j,i)
            dp[j] = world[i][1]        
        else :
            pass

        #안 쓸 경우
        dp[j] = max(dp_pre[j], dp[j])

print(dp[D])