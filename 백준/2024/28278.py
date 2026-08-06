# 28278 - 스택 2

import sys
input = sys.stdin.readline
n = int(input())
s = []
for _ in range(n):
    a = input().split()
    if a[0] == '1': s.append(a[1])
    elif a[0] == '3': print(len(s))
    elif len(s) > 0:
        if a[0] == '2': print(s.pop())
        elif a[0] == '4': print(0)
        elif a[0] == '5': print(s[-1])
    else:
        if a[0] == '4': print(1)
        else: print(-1)