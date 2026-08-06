# 1934 - 최소공배수

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = 1
    for i in range(2, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            while n % i == 0 and m % i == 0:
                n //= i
                m //= i
                a *= i
    print(a*n*m)

#-------------------------------

import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(math.lcm(n, m))