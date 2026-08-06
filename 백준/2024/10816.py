# 10816 - 숫자 카드 2

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

d = {}
for i in a:
    if i in d: d[i] += 1
    else: d[i] = 1
for i in q:
    if i in d: print(d[i], end=" ")
    else: print(0, end=" ")