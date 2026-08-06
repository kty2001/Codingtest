# 26069 - 붙임성 좋은 총총이

import sys
input = sys.stdin.readline
n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    if a == "ChongChong" or b == "ChongChong":
        d[a] = True
        d[b] = True
    elif a in d and d[a] == True: d[b] = True
    elif b in d and d[b] == True: d[a] = True
print(len(d))

#------------------------------------

import sys
n = int(sys.stdin.readline().strip())
member = set(['ChongChong'])
for _ in range(n) :
    p = list(sys.stdin.readline().split())
    if (p[0] in member) or (p[1] in member) :
        member.add(p[0])
        member.add(p[1])
print(len(member))