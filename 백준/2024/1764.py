# 1764 - 듣보잡

from sys import stdin as s
input = s.readline

n, m = map(int, input().split())
d = {}
a = []
for _ in range(n):
    p = input().rstrip()
    d[p] = 0
for _ in range(m):
    p = input().rstrip()
    if p in d: a.append(p)
print(len(a), *sorted(a), sep="\n")