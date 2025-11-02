import sys

N = int(sys.stdin.readline().strip())

world = list(map(int, sys.stdin.readline().split()))

world.sort()

if len(world)>=3:
    result = 2
    for i in range(len(world)-2):
        end = i+2
        while True:
            if world[i]+world[i+1] > world[end]:
                result = max(result, end-i+1)
                end+=1
                if len(world)==end:
                    break
            else:
                break
        pass
    print(result)
else:
    print(len(world))