# 2745 - 진법 변환

n, b = input().split()
ans = 0
for i, a in enumerate(n[::-1]):
    try:
        a = int(a)
    except:
        a = ord(a) - 55
    ans += a * (int(b) ** i)
print(ans)

# -----------------------------------

n, b = input().split()
print(int(n, int(b)))