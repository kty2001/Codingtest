# 18258 - 큐 2

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    t = input().split()
    if "push" == t[0]: q.append(t[1])
    elif "size" == t[0]: print(len(q))
    elif q:
        if "front" == t[0]: print(q[0])
        elif "back" == t[0]: print(q[-1])
        elif "empty" == t[0]: print(0)
        elif "pop" == t[0]: print(q.popleft())
    elif not q and t[0] == "empty": print(1)
    else: print(-1)
