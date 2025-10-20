import sys

N, K = map(int, sys.stdin.readline().split())


def cut():
    s = N+2
    low = 1
    high = s//2
    
    while low<=high:
        mid = (low+high) //2
        val = mid*(s-mid)
        
        if val == K:
            print("YES")
            return
        if val < K:
            low = mid + 1
        else:
            high = mid - 1

    print("NO")
    return 

    pass

cut()


