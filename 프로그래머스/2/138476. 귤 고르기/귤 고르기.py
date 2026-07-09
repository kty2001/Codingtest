def solution(k, tangerine):
    from collections import Counter
    answer = 0
    cnt = Counter(tangerine)
    for i, v in sorted(list(cnt.items()), key=lambda x: x[1], reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            return answer