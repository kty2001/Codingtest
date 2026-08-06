# 5073 - 삼각형과 세 변

import sys
input = sys.stdin.readline

while True:
    p = sorted(list(map(int, input().split())))
    if sum(p) == 0: break
    if p[2] >= p[1] + p[0]: print("Invalid")
    elif p[0] == p[1] == p[2]: print("Equilateral")
    elif p[0] == p[1] or p[1] == p[2]: print("Isosceles")
    else: print("Scalene")
