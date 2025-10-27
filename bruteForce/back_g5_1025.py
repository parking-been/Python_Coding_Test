import sys

N, M = map(int,sys.stdin.readline().split())

world = []
maxi = -1
for i in range(N):
    array = list(sys.stdin.readline().strip())
    world.append(array)

def cal(S):
    S = int(S)

    return S==int((S)**0.5)**2
    pass

for i in range(N): #첫 시작 부분
    for j in range(M): #첫 시작 부분
        for k in range(-N,N): #차 부분
            for t in range(-M, M): #차 부분
                S=""
                x = i
                y = j

                while 0<=x<N and 0<=y<M:
                    S = S+world[x][y]
                    #print(S)
                    
                    if cal(S):
                        maxi = max(maxi, int(S))
                    x =x+k
                    y =y+t
                    if k==0 and t==0:
                        break
                    pass

print(maxi)        