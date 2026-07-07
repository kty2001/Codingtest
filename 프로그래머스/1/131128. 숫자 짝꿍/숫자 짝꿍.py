def solution(X, Y):
    dig = {str(i): min(X.count(str(i)), Y.count(str(i))) for i in range(10)}
    answer = ''.join(k*v for k, v in dig.items())[::-1]
    if not answer: return '-1'
    if len(answer) == answer.count('0'): return '0'
    return answer