import sys
from collections import deque

move = [-1,1]
N, K = map(int, sys.stdin.readline().split())

sam = list(map(int,sys.stdin.readline().split()))

#메모리 오류 시간 오류 난다. 
def bfs():
    visited = set()
    queue = deque()
    count = 0
    sum = 0
    for e in sam:
        queue.append((e,e))
        visited.add(e)
    while queue:
        cur,e = queue.popleft()
        for v in move:
            next = cur+v
            if not next in visited:
                count+=1
                visited.add(next)
                queue.append((next,e))
                sum+=abs(next-e)

            if count==K:
                return sum
                pass    
        pass

    pass

print(bfs())