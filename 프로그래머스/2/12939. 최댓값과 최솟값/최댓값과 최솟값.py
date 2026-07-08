def solution(s):
    ans = set(map(int, s.split()))
    return f'{min(ans)} {max(ans)}'