# 25501 - 재귀의 귀재

import sys
input = sys.stdin.readline
def recursion(s, l, r, c):
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c+1)

t = int(input())
for i in range(t):
    s = input().rstrip()
    print(*recursion(s, 0, len(s)-1, 1))