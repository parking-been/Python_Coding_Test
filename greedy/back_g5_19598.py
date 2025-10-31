import sys
import heapq

N = int(sys.stdin.readline().strip())

world = []

for _ in range(N):
    world.append(list(map(int,sys.stdin.readline().split())))

world.sort(key=lambda x:x[0])

room = []
for ele in world:
    
    if len(room)==0:
        heapq.heappush(room, ele[1])
    else:
        cur = room[0]
        if cur>ele[0]:
            heapq.heappush(room,ele[1])
        else:
            heapq.heappop(room)
            heapq.heappush(room,ele[1])

    pass
print(len(room))