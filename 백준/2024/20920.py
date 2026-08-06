# 20920 - 영단어 암기는 괴로워

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = []
d = {}
for _ in range(n):
    w = input().rstrip()
    if w in d: d[w] += 1
    else: d[w] = 1
l = [k for k in d if len(k) >= m]
l.sort(key=lambda x: (-d[x], -len(x), x))
print(*l, sep="\n")