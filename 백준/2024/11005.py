# 11005 - 진법 변환 2

n, b = map(int, input().split())
a = []
while n > 0:
    a.append(n % b)
    if 10 <= a[-1] <= 35:
        a[-1] = chr(a[-1]+55)
    n //= b
print(*a[::-1], sep="")
