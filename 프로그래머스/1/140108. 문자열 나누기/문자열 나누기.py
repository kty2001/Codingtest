def solution(s):
    answer = 1
    cnt = 1
    start = s[0]
    for i in range(1, len(s)):
        if cnt == 0:
            answer += 1
            start = s[i]
        if s[i] == start: cnt += 1
        else: cnt -= 1            
    return answer