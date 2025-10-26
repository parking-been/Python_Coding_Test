import sys

mapp = {'N':(-1,0) , 
        'W':(0,-1),
        'S':(1,0),
        'E':(0,1)}

N,M,R = map(int,sys.stdin.readline().split())

world = []
upOrDown = [[True]*(M) for _ in range(N)] 

for i in range(N):
    array = list(map(int,sys.stdin.readline().split()))
    world.append(array)



def attack(x,y,m):
    len=world[x][y]
    move = mapp[m]
    dx = x
    dy = y
    count = 0
    attackCount= 0
    if not upOrDown[dx][dy]:
        return 0 
    while True:
        
        if 0<=dx<N and 0<=dy<M:
            if len>count:
                if upOrDown[dx][dy]:
                    len = max(len,world[dx][dy]+count)
                    attackCount+=1
                    #print("중간확인", count,len)
                upOrDown[dx][dy] = False
                
                count +=1
                dx += move[0]
                dy += move[1]
                
                pass
            else:
                break
        else:
            break
        if len == count:
            break
        
        pass
    
    return attackCount
    pass

def defense(x,y):
    upOrDown[x][y] = True
    pass

attackCount = 0
for _ in range(R):
    #공격
    array = list(sys.stdin.readline().split())
    result = attack(int(array[0])-1 , int(array[1])-1, array[2])
    attackCount +=result
    #수비
    array = list(sys.stdin.readline().split())
    defense(int(array[0])-1 , int(array[1])-1)
    

print(attackCount)
for ele in upOrDown:
    for e in ele:
        print('S' if e==True else 'F', end=" ")
    print()
