import sys
import heapq

N = int(sys.stdin.readline().strip())

min = []
max = []
visited = set()
visited_detail = {}
for i in range(N):
    P, L = map(int, sys.stdin.readline().split())
    heapq.heappush(min,(L,P)) # for -1
    heapq.heappush(max,(-L,-P)) # for 1
    visited_detail[P] = L
M = int(sys.stdin.readline().strip())

result = []
for i in range(M):
    array = list(sys.stdin.readline().split())

    if array[0]=='add':
        P = int(array[1])
        L = int(array[2])
        if P in visited:
            visited.remove(P)
        visited_detail[P] = L
        heapq.heappush(min,(L,P)) # for -1
        heapq.heappush(max,(-L,-P)) # for 1

    elif array[0] == 'recommend':
        flag = int(array[1])
        if flag==-1:
            while True:
                L,P= heapq.heappop(min)
                if not P in visited and L == visited_detail[P]:
                    result.append(P)
                    heapq.heappush(min,(L,P))
                    #visited.add(P)
                    break
            pass
        else:
            while True:
                L,P= heapq.heappop(max)
                L = -L ; P = -P
                if not P in visited and L == visited_detail[P]:
                    result.append(P)
                    heapq.heappush(max,(-L,-P))
                    #visited.add(P)
                    break
            pass
            
        pass
    elif array[0] =="solved":
        P = int(array[1])
        visited.add(P)
        del visited_detail[P]
        pass
    
    pass

for i in result:
    print(i)