# 2108 - 통계학

import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
c = {}
for i in a:
    if i not in c: c[i] = 1
    else: c[i] += 1
m = max(c.values())
b = []
for i in c:
    if c[i] == m and len(b) < 2:
        b.append(i)
print(round(sum(a)/n))
print(a[n//2])
print(b[-1])
print(a[-1] - a[0])