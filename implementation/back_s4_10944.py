import sys

N = int(sys.stdin.readline().strip())

T = (N-1)*4 + 1

world = [[' ']*T for _ in range(T)]


def check(x,n):
    for i in range(n):
        world[x+i][x]='*'
        world[x][x+i]='*'
        world[x+i][x+n-1]='*'
        world[x+n-1][x+i]='*'
    pass


count = 0
cur_t = T
while cur_t>=0:
    check(count,cur_t)
    count+=2
    cur_t -=4
    pass

for ele in world:
    print("".join(ele))
