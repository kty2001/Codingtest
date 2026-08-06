# 9063 - 대지

import sys
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))
p = list(zip(*p))
print((max(p[0])-min(p[0]))*(max(p[1])-min(p[1])))