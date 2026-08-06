# 14425 - 문자열 집합

n, m = map(int, input().split())
a = set()

for i in range(n):
    a.add(input().rstrip())

c = 0
for i in range(m):
    q = input().rstrip()
    if q in a:
        c += 1
print(c)

#--------------------------

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