def solution(n, lost, reserve):
    answer = 0
    ans = [1] * (n+1)
    for i in range(1, n+1):
        if i in lost: ans[i] -= 1
        if i in reserve: ans[i] += 1
        
    for i in range(1, n+1):
        if ans[i] == 0:
            if i > 0 and ans[i-1] == 2:
                ans[i] = ans[i-1] = 1
            elif i < n and ans[i+1] == 2:
                ans[i] = ans[i+1] = 1
    return sum(min(1, ans[i]) for i in range(1, n+1))