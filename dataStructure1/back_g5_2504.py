import sys
from collections import deque
array = list(sys.stdin.readline().strip())
stack = deque()
sum=0
tmp=1

for i in range(len(array)):
    
    cur = array[i]
    if cur=="(":
        stack.append(cur)
        tmp *=2
        pass
    elif cur == "[":
        stack.append(cur)
        tmp *=3
        pass
    elif cur == ")":
        if len(stack)==0 or stack[-1]!="(":
            sum = 0
            break
        stack.pop()
        if array[i-1]=="(":
            sum +=tmp
        tmp//=2
        pass
    else :
        if len(stack)==0 or stack[-1]!="[":
            sum = 0
            break
        stack.pop()
        if array[i-1]=='[':
            sum +=tmp
        tmp//=3
        pass
    #print(sum)
    pass

if stack:
    print(0)
else : print(sum)