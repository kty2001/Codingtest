# 10815 - 숫자 카드

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
d = {}
for i in a:
    d[i] = 0
for j in q:
    print(1 if j in d else 0, end=' ')

#-------------------------------------

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
q = list(map(int, input().split()))

for check in q:
    low, high = 0, n-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if a[mid] > check:
            high = mid - 1
        elif a[mid] < check:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')