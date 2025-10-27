import sys

N, M = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

array = list(set(array))
array.sort()

len = len(array)
total = []
def solution(start,depth):
    if depth == M:
        for e in total : print(e, end=" ")
        print()
        return
    for i in range(start,len):
        
        total.append(array[i])
        
        solution(i,depth+1)
        
        total.pop()
    return
    pass
solution(0,0)