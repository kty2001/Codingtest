def solution(A,B):
    answer = 0
    a = sorted(A)
    b = sorted(B, reverse=True)
    answer = sum(a[i]*b[i] for i in range(len(A)))
    return answer