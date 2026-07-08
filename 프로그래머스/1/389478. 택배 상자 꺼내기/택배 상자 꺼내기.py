def solution(n, w, num):
    answer = 0
    f1, f2 = n // w, num // w
    s1, s2 = n % w, num % w
    if s1 == 0:
        f1 -= 1
        s1 = w
    if s2 == 0:
        f2 -= 1
        s2 = w
    if f1 % 2 == f2 % 2:
        if s1 < s2:
            answer = f1 - f2
        else:
            answer = f1 - f2 + 1
    else:
        if w - s1 < s2:
            answer = f1 - f2 + 1
        else:
            answer = f1 - f2
    
    return answer