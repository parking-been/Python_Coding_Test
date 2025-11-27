import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

# list에서 중복 없애는 법 -> set

arr.sort()

gg = []
for i in range(N-1):
    t = arr[i+1]-arr[i]
    if t>0:
       gg.append(t)

#역
gg.sort()

ggl = len(gg)

print(sum(gg[:ggl-K+1]))
 