#
import sys
import heapq
T = int(sys.stdin.readline())
visited = [False]*(1000000+1)
result = []
for _ in range(T):
    N = int(sys.stdin.readline())
    array_m = [] #최소힙
    array_h = [] #최대힙
    idx = 0
    for _ in range(N):
        
        c, n = sys.stdin.readline().split()
        n = int(n)

        if c == 'I':
            heapq.heappush(array_m, (n,idx))
            heapq.heappush(array_h, (-n,idx))
            visited[idx] = True
            idx+=1

        else :
            
            if n==-1:
                while array_m and not visited[array_m[0][1]]:
                    heapq.heappop(array_m) # 필요없는 것들 빼내기
                
                #최소값 삭제
                if len(array_m)>0:
                    x,cidx = heapq.heappop(array_m)
                    visited[cidx] = False
                #array_h.remove(-x)
                pass
            else:
                while array_h and not visited[array_h[0][1]]:
                    heapq.heappop(array_h) # 필요없는 것들 빼내기
                
                #최소값 삭제
                if len(array_h)>0:
                    x,cidx = heapq.heappop(array_h)
                    visited[cidx] = False

                #array_m.remove(-x)
    
    while array_m and not visited[array_m[0][1]]:
        heapq.heappop(array_m) # 필요없는 것들 빼내기
    while array_h and not visited[array_h[0][1]]:
        heapq.heappop(array_h) # 필요없는 것들 빼내기

    
    if len(array_m)==0:
        result.append("EMPTY")
        #print("EMPTY")
    else:
        result.append(str(-heapq.heappop(array_h)[0])+" "+str(heapq.heappop(array_m)[0]))
        
        #print(heapq.heappop(array_m))#최솟값
        #print(heapq.heappop(array_h))#최댓값   


for e in result:
    print(e)