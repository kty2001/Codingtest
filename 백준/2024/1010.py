# 1010 - 다리 놓기

import sys
input = sys.stdin.readline
def f(x):
    r = 1
    for i in range(2, x+1):
        r *= i
    return r
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(f(k)//f(n)//f(k-n))