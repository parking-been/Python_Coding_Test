import sys
from collections import deque
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

def bfs(T):
    q = deque()
    q.append(T)
    while q:
        cur = q.popleft()
        if cur == '': continue

        if cur == S:
            return 1



        if cur[-1]=='A':
            #1번
            q.append(cur[:-1])
            #print(cur[:-1])
            pass
        if cur[0]=='B':
            #2번
            tmp = cur[1:]
            #print(tmp[::-1])
            q.append(tmp[::-1])

            pass
                

        pass
    pass

    return 0

print(bfs(T))