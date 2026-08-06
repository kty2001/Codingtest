# 11866 - 요세푸스 문제 0

from collections import deque
n, k = map(int, input().split())
d = deque(range(1, n+1))
a = []
while d:
    d.rotate(-k+1)
    a.append(d.popleft())
print(f"<{str(a)[1:-1]}>")

#---------------------------------------

n, k = map(int, input().split())
l = list(range(1, n + 1))
a = 0
p = []
while len(l) > 0:
    a = (a + k - 1) % len(l)
    p.append(l.pop(a))
print(f"<{str(p)[1:-1]}>")