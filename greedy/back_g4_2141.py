import sys

N = int(sys.stdin.readline().strip())
arr = []
total_count = 0

for i in range(N):
    x, a = map(int ,sys.stdin.readline().split())
    arr.append((x,a))
    total_count+=a

arr.sort()

tmp_count = 0
half_count = round(total_count/2)
for i in range(N):
    tmp_count+=arr[i][1]
    if tmp_count >= half_count:
        print(arr[i][0])
        break
        pass
