import sys
import heapq

N = int(sys.stdin.readline().strip())

total_list = []
for i in range(N):
    total_list.append(list(map(int,sys.stdin.readline().split())))
    pass
total_list.sort(key = lambda x : (x[0], x[1]))

room = []
for ele in total_list:
    if len(room)==0 or ele[0]<room[0]:
        #추가하기
        heapq.heappush(room, ele[1])
        pass
    else:
        cur = heapq.heappop(room)
        heapq.heappush(room,ele[1])
        pass

print(len(room))