import sys

N = int(sys.stdin.readline().strip())

weight = []
power = []
crack = [False]*N

for i in range(N):
    p, w = map(int,sys.stdin.readline().split())
    weight.append(w)
    power.append(p)

maxi = 0

def solution(depth):

    if depth==N:
        global maxi
        maxi = max(maxi, crack.count(True))
        # print(crack)
        # print(weight)
        # print(power)
        # print("디버깅목적")
        # print("디버깅용",maxi)
        # print("~~~~~~~~~")
        return
        pass

    if crack[depth]:
        solution(depth+1)
        return
        pass

    c_p = power[depth]
    
    if crack.count(True)==N-1:
        solution(depth+1)
        return
        pass
    for i in range(N):
        if i==depth:
            continue
        if not crack[i] :
            t_p = power[i]
            power[depth] = power[depth] - weight[i]
            if power[depth]<=0:
                crack[depth] = True
            power[i] = power[i] - weight[depth]
            if power[i]<=0:
                crack[i] = True
            solution(depth+1)
            power[i] = t_p
            power[depth] = c_p
            crack[i] = False
            crack[depth] = False



    pass

solution(0)
print(maxi)