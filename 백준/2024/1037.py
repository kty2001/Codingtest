# 1037 - 약수

n = int(input())
a = sorted(list(map(int, input().split())))
if n % 2 == 1:
    print(a[len(a)//2]**2)
else:
    print(a[0] * a[-1])