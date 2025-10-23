import sys
# 굳이 dp 로 안풀어도 됬을듯

N = int(sys.stdin.readline().strip())

world = [['.']*(N+2)]
bomb = []
dp = [[0]*(N+2) for _ in range(N+2)]
for i in range(1,N+1):
    array = list(sys.stdin.readline().strip())
    tmp = 0
    for j in range(N):
        if array[j]=='*':
            tmp+=1
            bomb.append((i-1,j))
        dp[i][j+1] = tmp + dp[i-1][j+1]
    world.append(['.']+array+['.'])
world.append(['.']*(N+2))

for j in range(N):
    dp[N+1][j+1] = dp[N][j+1] 
            

def block(x,y):
    a = max(1, x-1)
    b = max(1, y-1)
    c = min(N, x+1)
    d = min(N, y+1)
    count = dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1]
    return count
    pass

def checking(x,y):
    ff = 0
    if world[x][y] == '*':
        ff = 1
    return block(x,y) - ff, ff

f_total = 0
check = [['.']*(N) for _ in range(N)]
for i in range(1,N+1):
    array = list(sys.stdin.readline().strip())
    for j in range(1,N+1):
        if array[j-1]=='x':
            count, flag = checking(i,j)
            f_total = f_total or flag #or 처리 안해줬다..
            check[i-1][j-1] = str(count) #문자열로 바꿔준다.

if f_total == 1:
    for b in bomb:
        check[b[0]][b[1]] = '*'

for row in check:
    print(''.join(row))

