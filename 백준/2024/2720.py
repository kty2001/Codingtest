# 2720 - 세탁소 사장 동혁

n = int(input())
for i in range(n):
    c = int(input())
    print(c // 25, end=" ")
    c %= 25
    print(c // 10, end=" ")
    c %= 10
    print(c // 5, end=" ")
    c %= 5
    print(c)