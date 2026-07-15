def solution(priorities, location):
    from collections import deque as dq
    answer = 0
    pri = dq([i, p] for i, p in enumerate(priorities))
    while True:
        cur = pri.popleft()
        if any(cur[1] < p[1] for p in pri):
            pri.append(cur)
        else:
            answer += 1
            if cur[0] == location: return answer