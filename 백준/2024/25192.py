# 25192 - 인사성 밝은 곰곰이

import sys
input = sys.stdin.readline
n = int(input())
c = 0
f = {}
for i in range(n):
    s = input().rstrip()
    if s == "ENTER":
        c += len(f)
        f = {}
    else: f[s] = True
c += len(f)
print(c)

#--------------------------------

print(sum(len({*s.split()})for s in open(0).read().split('ENTER'))-1)