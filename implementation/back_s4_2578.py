import sys

world = []
side = [0]*5
up = [0]*5
tri = [0]*2
mapp = {}

for i in range(5):
    array = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        mapp[array[j]] = (i,j)
    world.append(array)


def update(x,y):
    side[x]+=1
    up[y]+=1
    if (x==y) : tri[0]+=1
    if (x+y==4) : tri[1]+=1

def check(arrayi):
    count = 0
    for ele in arrayi:
        if ele==5:
            count+=1
    return count

total_result = 0

for i in range(5):
    commend = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        cur = commend[j]
        x,y = mapp[cur]
        update(x,y)
        sum = 0
        sum+=check(side)
        sum+=check(up)
        sum+=check(tri)
        if sum>=3:
            total_result = (i*5+j)+1
            break
    if total_result!=0:
        break

print(total_result)