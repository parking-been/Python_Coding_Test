import sys

data = list(sys.stdin.readline().strip())

def solution():
    stack = []
    pipe = []
    count = 0
    pre = '.'
    for e in data:
        if e=='(':
            stack.append(count)
            pass
        else :
            if pre=='(':
                #레이저
                stack.pop()
                count+=1
            else:
                #쇠 막대기
                x = stack.pop()
                pipe.append(count-x)
                pass
        pre = e
        #print("c",e,"stack",stack)
    len2=len(pipe)
    print(sum(pipe)+len2)
    pass

solution()