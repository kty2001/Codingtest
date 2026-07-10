def solution(n):
    fi = {0: 1, 1: 1}
    for i in range(2, n+1):
        fi[i] = fi[i-1] + fi[i-2]
    return fi[n]%1234567