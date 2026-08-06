# 1978 - 소수 찾기

n = int(input())
a = [0 for _ in range(1001)]
for i in range(2, 501):
    if a[i] == 1: continue
    for j in range(i+1, 1001):
        if j % i == 0:
            a[j] = 1
m = list(map(int, input().split()))
cnt = 0
for i in m:
    if i == 1: continue
    elif a[i] == 0: cnt += 1
print(cnt)