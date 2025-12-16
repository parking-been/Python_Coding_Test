import sys

N, K = map(int, sys.stdin.readline().split())

student = list(map(int, sys.stdin.readline().split()))
between = []

for i in range(N-1):
    between.append(student[i+1]-student[i])

between.sort()

sum = 0
for i in range(N-K):
    sum+=between[i]
print(sum)