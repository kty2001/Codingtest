# 14215 - 세 막대

p = sorted(list(map(int, input().split())))
if p[0] + p[1] <= p[2]:
    p[2] = p[0] + p[1] - 1
print(sum(p))