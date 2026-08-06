# 2566 - 최댓값

ans = 0
r, c = 0, 0
for i in range(9):
    arr = list(map(int, input().split()))
    if ans < max(arr):
        ans = max(arr)
        r = i
        c = arr.index(ans)
print(f'{ans}\n{r+1} {c+1}')