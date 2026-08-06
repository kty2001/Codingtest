# 2331 - 분해합

n = int(input())
for i in range(max(n - len(str(n))*9, 1), n):
    if i+sum(map(int, str(i))) == n:
        print(i)
        break
else: print(0)