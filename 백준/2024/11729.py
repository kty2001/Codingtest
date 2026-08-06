# 11729 - 하노이 탑 이동 순서

def h(n, s, f, a):
    if n == 1: return print(s, f)
    h(n-1, s, a, f)
    print(s, f)
    h(n-1, a, f, s)

n = int(input())
print(2**n - 1)
h(n, 1, 3, 2)