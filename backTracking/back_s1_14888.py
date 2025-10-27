import sys

N = int(sys.stdin.readline().strip())

array = list(map(int,sys.stdin.readline().split()))
m_array = list(map(int,sys.stdin.readline().split()))

INF = int(1e9)

maxi = -INF
mini = INF

def solution(result,depth):
    if depth==N:
        global maxi
        global mini
        maxi = max(maxi, result)
        mini = min(mini, result)
        return
    
    
    for i in range(4):
        if m_array[i]!=0:
            
            val = calculate(result,array[depth],i)
            #print("중간 결과", val)
            m_array[i]-=1
            solution(val, depth+1)
            m_array[i]+=1
            
            pass
        pass

    pass

def calculate(x, y, i):
    if i==0:
        return x+y
    elif i==1:
        return x-y
    elif i==2:
        return x*y
    else:
        if x<0:
            return -(abs(x)//y)
        elif x==0: #예외 처리 how?-> 안해도 문제 푸는데는 이상이 없다.
            return 0
        else : 
            return (abs(x)//y)
        
solution(array[0],1)
print(maxi)
print(mini)