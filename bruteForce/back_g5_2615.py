import sys

map = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
move=[[[0,-1],[0,1]], #가
      [[-1,0],[1,0]], #세
      [[-1,-1],[1,1]], #대1
      [[1,-1],[-1,1]], #대2
      
      ]
black = []
white = []
for i in range(19):
    for j in range(19):
        if map[i][j] == 1:
            #검은 돌
            black.append((i,j))
        elif map[i][j]==2:
            #흰돌
            white.append((i,j))

def solution(color, location):
    my = color
    for m in move:
        left= m[0]
        right = m[1]
        
        l_x = location[0]+left[0]
        l_y = location[1]+left[1]
        r_x = location[0]+right[0]
        r_y = location[1]+right[1]
        flag =0
        if l_x<0 or l_x>=19 or l_y<0 or l_y>=19:
            flag = 1
        elif map[l_x][l_y]!=my:
            flag= 1 
        if r_x<0 or r_x>=19 or r_y<0 or r_y>=19:
            continue

        if flag==1 and map[r_x][r_y]==my:
            #왼쪽 다른거 오른쪽 나
            cur_location = list(location[:])
            count = 1
            while True:
                cur_location[0]= cur_location[0]+right[0]
                cur_location[1] = cur_location[1]+right[1]
                #print(">",cur_location)
                
                if cur_location[0]>=19 or cur_location[1]>=19 or cur_location[1]<0 or cur_location[0]<0:
                    break 

                cur = map[cur_location[0]][cur_location[1]]
                
                if cur==my:
                    count+=1
                else:
                    break

            pass 
            
            if count == 5:
                return location

    return (-1,-1)
    pass

#print(black)
#exit()
#검은돌 승패 확인하기.
for e in black:
    result = solution(1,e)
    if result !=(-1,-1):
        print(1)
        print(result[0]+1, result[1]+1)
        exit()
    pass

for e in white:
    result = solution(2,e)
    if result !=(-1,-1):
        print(2)
        print(result[0]+1, result[1]+1)
        exit()
    pass

print(0)