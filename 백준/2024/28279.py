# 28279 - 덱 2

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
d = deque()
for _ in range(n):
    a = input().split()
    if a[0] == '1': d.appendleft(a[1])
    elif a[0] == '2': d.append(a[1])
    elif a[0] == '3':
        if d: print(d.popleft())
        else: print(-1)
    elif a[0] == '4':
        if d: print(d.pop())
        else: print(-1)
    elif a[0] == '5': print(len(d))
    elif a[0] == '6':
        if d: print(0)
        else: print(1)
    elif a[0] == '7':
        if d: print(d[0])
        else: print(-1)
    elif a[0] == '8':
        if d: print(d[-1])
        else: print(-1)