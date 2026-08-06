# 2346 - 풍선 터트리기

from collections import deque
n = int(input())
a = list(map(int, input().split()))
d = deque()
for i, j in enumerate(a):
    d.append([i+1, j])
a = []
for _ in range(n):
    r = d.popleft()
    a.append(r[0])
    if r[1] > 0: d.rotate(-(r[1]-1))
    else: d.rotate(-r[1])
print(*a)