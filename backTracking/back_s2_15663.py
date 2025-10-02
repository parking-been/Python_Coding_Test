import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().split())


data = list(map(int,sys.stdin.readline().split()))

data.sort()
answer = []
visited = [False]*(N)
def solution():
   
    if len(answer)==M:
        print(' '.join(map(str,answer)))
        #print(visited)
    pre = -1
    for i in range(N):
        
        if not visited[i] and pre!=data[i]:
            visited[i] = True
            answer.append(data[i])
            solution()
            answer.pop()
            visited[i] = False
            pre = data[i]
            pass

            
    pass

solution()