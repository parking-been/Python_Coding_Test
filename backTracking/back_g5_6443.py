import sys
from collections import Counter
T = int(sys.stdin.readline().strip())

def solution(depth):
    if depth == total_leg:
        print("".join(total))
        pass

    for i in range(length):
        if s_count[i]!=0:
            total.append(s_array[i])
            s_count[i]-=1
            solution(depth+1)
            total.pop()
            s_count[i]+=1
            pass
    pass

for _ in range(T):
    total=[]
    array = list(sys.stdin.readline().strip())
    total_leg = len(array)
    
    s_array = list(set(array))
    s_array.sort()
    length = len(s_array)
    s_count = [0]*(length)
    for e in array:
        s_count[s_array.index(e)]+=1

    
    solution(0)
    
    