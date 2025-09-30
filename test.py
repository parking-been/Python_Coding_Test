arr = [1,2,3,4]

print(" ".join(map(str, arr))) #1 2 3 4
print(*arr) #1 2 3 4

a=2
b=1
res = a if a > b else b
print(res)