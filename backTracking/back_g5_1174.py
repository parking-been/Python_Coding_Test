import sys
from collections import deque
N = int(sys.stdin.readline().strip())

def bfs():
    q = deque(list(range(10)))
    idx= 0 
    while q:
        cur = q.popleft()
        idx+=1
        if idx ==N:
            print(cur)
            return
        for i in range(cur%10):
            m = cur*10 +i
            q.append(m)

    print(-1)
    pass

bfs()