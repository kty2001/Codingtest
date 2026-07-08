def solution(s):
    answer = ''
    s = s.replace(' ', ' * ').split()
    for a in s:
        if a == '*':
            answer += ' '
        else:
            answer += a[0].upper() + a[1:].lower()
    return answer