# 7785 - 회사에 있는 사람

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = {}
for i in range(n):
    a[input()] = 0
c = 0
for i in range(m):
    q = input()
    if q in a:
        c += 1
print(c)