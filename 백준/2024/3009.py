# 3009 - 네 번째 점

x = []
y = []
for _ in range(3):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)
print((max(x)+min(x))*2 - sum(x), (max(y)+min(y))*2 - sum(y))