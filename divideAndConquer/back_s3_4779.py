import sys


def solution(x, y,array):
    #0~9
    interv = y-x
    if interv ==1:
        array[x] = '-'
        return
    div = int(interv/3)
    solution(x,x+div,array)
    solution(x+div*2,x+div*3,array)

    pass



while True:

    N = sys.stdin.readline().strip()
    if N == "":
        break
    N = int(N)
    tmp = pow(3,N)
    array = [' ']*tmp
    solution(0,tmp,array)

    for e in array : print(e, end='')
    print()