# 2581 - 소수

n = int(input())
m = int(input())
a = [1 for _ in range(10001)]
for i in range(2, 5001):
    if a[i] == 0: continue
    for j in range(i+1, 10001):
        if j % i == 0:
            a[j] = 0
h = 0
c = -1
for i in range(n, m+1):
    if i == 1: continue
    if a[i] == 1:
        if h == 0: c = i
        h += i
if h == 0: print(c)
else: print(h,"\n", c, sep="")