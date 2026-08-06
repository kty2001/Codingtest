# 2485 - 가로수

import sys
import math
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
b = []
for i in range(n-1):
    b.append(a[i+1]-a[i])
g = math.gcd(*b)
r = len(range(a[0], a[-1]+1, g))
print(r-n)