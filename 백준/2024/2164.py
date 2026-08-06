# 2164 - 카드2

from collections import deque
n = int(input())
q = deque(range(1, n+1))
while len(q) > 1:
    t = q.popleft()
    q.append(q.popleft())
print(*q)

#--------------------------------------

n = int(input())
i = 0.5
while i*2 < n:
    i *= 2
print(int((n - i) * 2))