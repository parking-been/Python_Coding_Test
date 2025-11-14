import sys

N = int(sys.stdin.readline().strip())

train = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())

box = list(map(int, sys.stdin.readline().split()))

visited = [False]*M
pos = [0]*N
totalCount = M
train.sort(reverse = True)
box.sort(reverse = True)
time = 0

if box[0] > train[0]:
    print(-1)
    sys.exit(0)

while totalCount> 0 :
    for tt in range(N):
        while pos[tt]<M:
            cc = pos[tt]
            if not visited[cc] and train[tt]>=box[cc]:
                visited[cc] = True
                totalCount-=1
                pos[tt]+=1
                break
            pos[tt] +=1
    time +=1
    pass

print(time)