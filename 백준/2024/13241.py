# 13241 - 최소공배수

import math
n, m = map(int, input().split())
print(math.lcm(n, m))

#---------------------------------

a,b=map(int,input().split())
m,n=a,b
while m!=0:
    m,n=n%m,m
print(a*b//n)