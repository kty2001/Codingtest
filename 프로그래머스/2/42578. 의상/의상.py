def solution(clothes):
    clo = {}
    for c, t in clothes:
        if t in clo: clo[t] += 1
        else: clo[t] = 1
    
    ans = 1
    for c in list(clo.values()):
        ans *= c + 1
    return ans - 1