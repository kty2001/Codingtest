# 27433 - 팩토리얼 2

def f(n):
    if n < 2: return 1
    return n*f(n-1)
n = int(input())
if n == 0: print(1)
else: print(f(n))