import sys
from collections import deque
N = int(sys.stdin.readline())
move = [[0,1,2], #가로
        [3,4,5],
        [6,7,8],
        # 세로
        [0,3,6],
        [1,4,7],
        [2,5,8],
        #대각선
        [0,4,8],
        [2,4,6]
        
        ]

def ten2two(x):
    return list(bin(x)[2:].zfill(9))
    pass

def two2ten(list):
    return ( int(''.join(list),2) ) #291

def bfs(list):
    q = deque()
    visited = [False]*512 #1111111-> 511
    x = two2ten(list)
    visited[x] = True
    q.append((x,0))
    
    if x==0 or x==511:
        return 0

    while q:
        cur,dis = q.popleft()
        cur_l = ten2two(cur)
        
        for e in move:
            cur_le = cur_l[:]   #얕은 복사 문제 정리하기
            for i in e:
                cur_le[i] = ('1'if cur_le[i]=='0' else '0')

            new_x = two2ten(cur_le)
            if not visited[new_x]:
                visited[new_x] = True
                
                if new_x==0 or new_x==511:
                    return dis+1
                    
                q.append((new_x,dis+1))

        pass
    
    return -1

    pass


result = []
for _ in range(N):
    #각 case풀기
    #입력
    total_list = []
    for _ in range(3):
        board = list(sys.stdin.readline().split())
        for e in board:
            if e=='H':
                total_list.append('1')
            else:
                total_list.append('0')

    result.append(bfs(total_list))

for e in result:
    print(e)
    
    
    