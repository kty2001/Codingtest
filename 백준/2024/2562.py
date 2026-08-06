# 2562 - 최댓값

ans = [0, 0]
for i in range(1,10):
    n = int(input())
    if ans[0] < n:
        ans[0] = n
        ans[1] = i
print(ans[0])
print(ans[1])