# 2798 - 블랙잭

from itertools import combinations as c
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(c(a, 3))
h = 0
for i in b:
    if sum(i) == m:
        h = m
        break
    elif sum(i) < m and sum(i) > h:
        h = sum(i)
print(h)