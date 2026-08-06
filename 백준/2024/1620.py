# 1620 - 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p = {}
for i in range(n):
    a = input().rstrip()
    p[a] = str(i+1)
    p[str(i+1)] = a
for i in range(m):
    a = input().rstrip()
    if a in p: print(p[a])
