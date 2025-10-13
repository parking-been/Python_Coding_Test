import sys

N, M = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

s_array = list(set(array))

s_array.sort()

s_len = len(s_array)

def solution(strr,depth):
    ndepth = depth + 1
    for i in s_array:
        
        tmp = strr + " " + str(i)
        if ndepth == M:
            print(tmp.strip())
            
            pass
        else:
            solution(tmp, ndepth)

        pass    
    pass

solution("",0)