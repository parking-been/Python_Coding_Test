import sys
from itertools import combinations
N = int(sys.stdin.readline().strip())

world = []

for _ in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    world.append(array)

total_list = []
all = list(range(N))

total_sum = 0
for eles in combinations(all, 2):
    total_sum-=world[eles[0]][eles[1]] + world[eles[1]][eles[0]] 


def calculate(sum,i):
    
    sum1 = 0
    for ele in total_list:
        sum1 += world[i][ele] + world[ele][i]
    
    not_total_list = [x for x in all if not x in total_list]
    sum2 = 0
    for ele in not_total_list:
        sum2 += world[i][ele] + world[ele][i]

    sum = sum + sum1 + sum2
    
    return sum

    #return sum


def solution(sum,depth):

    if depth==int(N/2):
        return


    if len(total_list)==0: last = -1
    else : last = total_list[-1]
    for i in range(last+1,N):
        total_list.append(i)
        value = calculate(sum, i)
        global mini
        mini = min(mini, abs(value))
        solution(value, depth+1)

        total_list.remove(i)

        pass

    pass


mini = int(1e9)

solution(total_sum,0)
print(mini)