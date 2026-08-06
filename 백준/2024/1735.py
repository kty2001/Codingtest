# 1735 - 분수 합

import math
a, b = map(int, input().split())
n, m = map(int, input().split())
x, y = a*m + n*b, b*m
d = math.gcd(x, y)
print(x//d, y//d)