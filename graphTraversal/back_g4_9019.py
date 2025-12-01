import sys
from collections import deque
import copy
C = 10000
T = int(sys.stdin.readline().strip())
commands = ['D', 'S', 'L', 'R']

def solution(N, command):
    if command=='D':
        return (N*2)%C
    elif command == 'S':
        return (N-1)%C
    elif command == 'L' : 
        return ((N%1000)*10 + (N//1000))%C
    elif command=='R':
        return ((N%10)*1000 + (N//10))%C


def bfs(A,B):
    q = deque()
    visited = [False]*(C)
    pre = [0]*(C)
    preS = ['']*(C)
    q.append(A)
    visited[A] = True
    while q:
        cur = q.popleft()
        for c in commands:
            result = solution(cur, c)
            
            if result == B:
                llist = [c]
                t = cur
                
                while t!=A:
                    llist.append(preS[t])
                    t = pre[t]
                rlist = llist[::-1]
                return rlist
                
            if not visited[result]:
                q.append(result)
                visited[result] = True
                pre[result] = cur
                preS[result] = c
                pass
            
    return []
    pass       


for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    llist = bfs(A,B)
    print(''.join(llist))
    