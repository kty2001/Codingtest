# 24511 - queuestack

from collections import deque
n = int(input())
f = input().split()
d = input().split()
m = input()
a = input().split()
q = deque()
for i in range(n):
    if f[i] == '0': q.append(d[i])
for i in a:
    q.appendleft(i)
    print(q.pop(), end=" ")