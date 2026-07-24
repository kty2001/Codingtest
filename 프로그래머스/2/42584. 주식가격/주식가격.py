def solution(prices):
    answer = [0] * len(prices)
    s = []
    for i, p in enumerate(prices):
        while s and s[-1][1] > p:
            t, v = s.pop()
            answer[t] = i - t
        s.append([i, p])
    for i, v in s:
        answer[i] = len(prices) - i - 1
    return answer