def solution(prices):
    answer = [0] * len(prices)
    s = []
    # stack[-1]보다 다음 값이 크면 push, 아니면 pop 후 인덱스 차이 할당
    # prices 안남으면 pop 하면서 인덱스 차이 할당
    for i, p in enumerate(prices):
        if not s:
            s.append([i, p])
        else:
            if s[-1][1] <= p:
                s.append([i, p])
            else:
                while s and s[-1][1] > p:
                    t, v = s.pop()
                    answer[t] = i - t
                s.append([i, p])
        
    for i, v in s:
        answer[i] = len(prices) - i - 1
    return answer