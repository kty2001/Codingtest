def solution(n):
    cnt = 0
    while n > 0:
        if not n % 2:
            n //= 2
        else:
            n -= 1
            cnt += 1
    return cnt