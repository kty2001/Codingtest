# 2839 - 설탕 배달

n = int(input())
for i in range(1667):
    if n < 0:
        print(-1)
        break
    elif n % 5 == 0:
        print(i+n//5)
        break
    n -= 3