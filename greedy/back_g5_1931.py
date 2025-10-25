import sys
import heapq
N = int(sys.stdin.readline().strip())

q = []

for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    heapq.heappush(q,(b,a))

last = 0
count = 0

while q:
    b,a = heapq.heappop(q)
    if a>=last:
        count+=1
        last = b

    pass

print(count)