import sys
from collections import deque

N , K = map(int,sys.stdin.readline().split())

world = list(map(int, sys.stdin.readline().split()))

q = deque(world)

#print(q.count(2))

box = []
count =0
while(q.count(0)<K):
    q.rotate(1)
    
    new_box = []
    for x in box:
        if x<N-2:
            new_box.append(x+1)
    box = new_box
    for i in range(len(box)):
        
        if q[box[i]+1]!=0 and not(box[i]+1 in box):
            box[i]+=1
            q[box[i]]-=1
            pass
    
    if q[0]!=0:
        box.append(0)
        q[0]-=1

    count+=1
    pass

print(count)